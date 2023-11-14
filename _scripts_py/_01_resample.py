import os
import subprocess
from utils import ensure_paths_exist, find_files

def compare_files(input_files, output_files):
    files_to_process = [file for file in input_files if file not in output_files]
    return files_to_process

def resample_audio(input_file, output_file, sample_rate='16000'):
    command = ['ffmpeg', '-i', input_file,
               '-ar', sample_rate, output_file]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    input_folder = 'fs/_record_raw'
    output_folder = 'fs/_record_processed'
    ensure_paths_exist([input_folder, output_folder])

    input_files = find_files(input_folder, '.wav')
    output_files = find_files(output_folder, '.wav')
    print(input_files)
    print(output_files)

    files_to_process = compare_files(input_files, output_files)
    print(f"Liczba plików do przetworzenia: {len(files_to_process)}")
    print(files_to_process)


    for file in files_to_process:
        os.makedirs(os.path.dirname(os.path.join(output_folder, file)), exist_ok=True)
        print(f"Przetwarzanie pliku: {file}...")
        in_file = os.path.join(input_folder, file)
        out_file = os.path.join(output_folder, file)
        resample_audio(in_file, out_file)

main()