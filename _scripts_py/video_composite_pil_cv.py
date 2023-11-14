from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import os
import tempfile
import shutil
import time

# Funkcja do dodawania tekstu do ramki
def init_font(font_path, font_size):
    font = ImageFont.truetype(font_path, font_size)
    return font

def draw_text(image, text, position, font):
    draw = ImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=(255, 255, 255))

def process_video(input_video_file, output_video_file, font_file):
    text = "Twój tekst"
    font_size = 24
    position = (50, 50)

    # Otworzenie wideo do odczytu
    video = cv2.VideoCapture(input_video_file)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Ustawienie kodeka i tworzenie obiektu VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Odczytanie każdej ramki, dodanie tekstu i zapisanie
    i = 0
    font = init_font(font_file, font_size)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        print(i)
        i += 1

        # Konwersja ramki do obrazu PIL
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Rysowanie tekstu na obrazie
        draw_text(image, text, position, font)
        
        # Konwersja z powrotem do formatu ramki OpenCV
        frame_with_text = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Zapisanie ramki
        out.write(frame_with_text)

    # Zwolnienie zasobów
    video.release()
    out.release()

    # Informacja o zakończeniu procesu
    print("Wideo zostało przetworzone i zapisane jako", output_video_file)

def main():
    input_video = 'fs/_video_yt_split/hoe_math_levels_basic.mp4'
    output_video = 'fs/_video_yt_result/levels.mp4'
    font = 'C:/Windows/Fonts/arial.ttf'

    start = time.perf_counter()
    with tempfile.TemporaryDirectory() as virt_dir:
        print('Tymczasowy katalog:', virt_dir)
        input_video_virt = os.path.join(virt_dir, 'input.mp4')
        output_video_virt = os.path.join(virt_dir, 'output.mp4')
        font_virtual = os.path.join(virt_dir, 'font.ttf')
        shutil.copy2(input_video, input_video_virt)
        shutil.copy2(font, font_virtual)
        process_video(input_video_virt, output_video_virt, font_virtual)
        shutil.copy2(output_video_virt, output_video)
    stop = time.perf_counter()
    print(f"Czas wykonania: {stop - start:0.4f} sekund")

main()