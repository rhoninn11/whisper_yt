import os
import sys
from pytube import YouTube
from moviepy.editor import *
from utils import ensure_paths_exist

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write(f"\r +++ Pobieranie: {percentage_of_completion:.2f}%")
    sys.stdout.flush()

def download_video(video_url, output_path):
    yt = YouTube(video_url, on_progress_callback=progress_function)
    video_stream = yt.streams.get_by_resolution("720p")
    video_path = video_stream.download(output_path=output_path)
    return video_path

def split_audio_video(input_video_path, output_path, video_name):
    audio_output_path = os.path.join(output_path, f"{video_name}.wav")
    video_output_path = os.path.join(output_path, f"{video_name}.mp4")
    
    video = VideoFileClip(input_video_path)
    video.audio.write_audiofile(audio_output_path)
    video.write_videofile(video_output_path, codec='libx264', audio_codec='aac')
    
    video.close()

def main():
    if len(sys.argv) != 3:
        print("Użycie: python script.py <nazwa_pliku> <URL_filmiku_YouTube>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    video_url = sys.argv[2]

    download_folder = "fs/_video_yt"
    split_folder = "fs/_video_yt_split"
    ensure_paths_exist([download_folder, split_folder])


    # Pobierz filmik z YouTube
    downloaded_video_path = download_video(video_url, download_folder)
    print(f"Filmik został pobrany i zapisany w: {downloaded_video_path}")

    # Wyodrębnij ścieżki audio i wideo
    split_audio_video(downloaded_video_path, split_folder, file_name)
    print(f"Ścieżki audio i wideo zostały zapisane w: {split_folder}")

if __name__ == "__main__":
    main()
