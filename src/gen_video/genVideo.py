# 将图片 + 音频 转成 视频
# 使用 ffmpeg 将图片转视频，并设置时长为音频时长，然后给生成的视频添加audio

import glob
from moviepy.editor import *
import random

def create_video_from_images(output_path, image_list, frame_rate=24.0, audio_path=''):
    clips = []
    index = 0

    audio_clip = AudioFileClip(audio_path)
    every_duration = audio_clip.duration / len(image_list)

    # 必须保证图片的尺寸完全一致生成的视频才会正常，否则视频会闪动有噪音
    for path in image_list:
        frame = ImageClip(path).set_duration(every_duration).set_start(index)
        index += every_duration
        clips.append(frame)

    final_video = concatenate_videoclips(clips, method='chain')
    final_video.write_videofile(output_path, fps=frame_rate, codec='libx264')


def add_audio_to_video(video_path, audio_path):
    audio_clip = AudioFileClip(audio_path)
    video_clip = VideoFileClip(video_path)

    final_video = video_clip.set_audio(audio_clip)
    final_video.write_videofile(video_path)

# add_audio_to_video(video_path, audio_path)

def loop_create_video(img_path, audio_path, audio_file_extension='mp3', image_file_extension='jpg', output_path=''):
    # 循环audio_path，得到每个audio的路径，然后随机取一张图片，生成video
    audio_paths = glob.glob(os.path.join(audio_path, '*.' + audio_file_extension))
    img_paths = glob.glob(os.path.join(img_path, '*.' + image_file_extension))
    for audio in audio_paths:
        img = img_paths[random.randint(0, len(img_paths)) - 1]
        audio_name = os.path.basename(audio)
        video_path = output_path + '/' + audio_name.replace('.mp3', '.mp4')
        print(video_path, '开始生成')
        create_video_from_images(video_path, [img], 1, audio)
        add_audio_to_video(video_path, audio)
        print(video_path, '生成完毕')


loop_create_video('../static/imgs', '../static/audio', 'mp3', 'jpg', '../static/video')
