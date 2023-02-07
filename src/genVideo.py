# 将图片 + 音频 转成 视频
# 使用 ffmpeg 将图片转视频，并设置时长为音频时长，然后给生成的视频添加audio

import glob
from moviepy.editor import *

def create_video_from_images(output_path, image_input_dir, frame_rate=24.0, image_file_extension='jpg', audio_path=''):
    image_paths = glob.glob(os.path.join(image_input_dir, '*.' + image_file_extension))
    clips = []
    index = 0

    audio_clip = AudioFileClip(audio_path)
    every_duration = audio_clip.duration / len(image_paths)

    # 必须保证图片的尺寸完全一致生成的视频才会正常，否则视频会闪动有噪音
    for path in image_paths:
        frame = ImageClip(path).set_duration(every_duration).set_start(index)
        index += every_duration
        clips.append(frame)

    final_video = concatenate_videoclips(clips, method='chain')
    final_video.write_videofile(output_path, fps=frame_rate, codec='libx264')

# 先生成video，然后再给video加audio
video_path = '../static/video/许嵩_放肆.mp4'
img_path = '../static/imgs'
audio_path = '../static/audio/许嵩_放肆.flac'
print('图片生成视频 start')
create_video_from_images(video_path, '../static/imgs', frame_rate=1, audio_path=audio_path);
print('图片生成视频 end')

def add_audio_to_video(video_path, audio_path):
    audio_clip = AudioFileClip(audio_path)
    video_clip = VideoFileClip(video_path)

    final_video = video_clip.set_audio(audio_clip)
    final_video.write_videofile(video_path);

print('给视频添加音频 start')
add_audio_to_video(video_path, audio_path)
print('给视频添加音频 end')