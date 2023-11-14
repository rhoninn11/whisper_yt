import os

from utils import ensure_paths_exist, find_files

def transcribe_audio(in_file, out_file):
    pass

def main():
    input_folder = 'fs/_record_processed'
    output_folder = 'fs/_record_transcribed'
    ensure_paths_exist([input_folder, output_folder])

    files_to_process = find_files(input_folder, ".wav")

    for file in files_to_process:
        os.makedirs(os.path.dirname(os.path.join(output_folder, file)), exist_ok=True)
        print(f"Przetwarzanie pliku: {file}...")
        in_file = os.path.join(input_folder, file)
        out_file = os.path.join(output_folder, file)
        transcribe_audio(in_file, out_file)


main()