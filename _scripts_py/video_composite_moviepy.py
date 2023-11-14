
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import json

def create_text_composition(text, start, duration):
    txt_clip = TextClip(text, fontsize=50, color='white', bg_color='black')
    txt_clip = txt_clip.set_position('center').set_start(start).set_duration(duration)
    return txt_clip

def main():
    video_file = "fs/_video_yt_split/hoe_math_levels_basic.mp4"
    out_video_file = "s/_video_yt_split/hoe_math_levels_basic.mp4"
    sentence_file = "fs/_video_yt_split/hoe_math_levels_basic.sentence.json"

    napisy = json.load(open(sentence_file))
    video = VideoFileClip(video_file)

    text_clips = []
    for napis in napisy:
        text_clips.append(create_text_composition(napis["text"], napis["s_pos"], napis["s_length"]))

    video_with_txt = CompositeVideoClip([video] + text_clips)

    video_with_txt.write_videofile(out_video_file, fps=video.fps)

main()