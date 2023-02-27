from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
from gen_video.util import parse_lrc_file, get_current_text
# 设置要使用的字体

font_path = "./static/fonts/msyh.ttc"
font_size = 40
font = ImageFont.truetype(font_path, font_size)

# 加载图片
img_path = "./static/imgs/3.jpg"
img = Image.open(img_path)

# 加载歌词文件
lrc_path = "./static/lrcs/七号公园.lrc"
with open(lrc_path, 'r', encoding='gb18030', errors='ignore') as f:
    lrc = f.read()
lrc_map = parse_lrc_file(lrc_path)

# 加载音频文件
audio_path = "./static/audio/许嵩 - 七号公园.mp3"
audio = AudioFileClip(audio_path)

# 创建视频帧
duration = audio.duration
frames = []
for t in range(int(duration)):
    # t是循环的次数，如何将lrc时间和循环次数相匹配呢？
    # 获取当前时刻的歌词
    lrc_now = get_current_text(t, lrc_map) # todo: 根据当前时间戳从歌词中获取当前时刻的歌词
    # 在图片上绘制当前时刻的歌词
    img_now = img.copy()
    draw = ImageDraw.Draw(img_now)
    draw.text((50, 50), lrc_now, font=font, fill=(255, 255, 255))
    # 将图片转换为视频帧

    frame = ImageClip(np.array(img_now)).set_duration(1)
    frames.append(frame)

# 创建视频
video = concatenate_videoclips(frames)
video = video.set_audio(audio)

# 保存视频
output_path = "./static/outputs/output.mp4"
video.write_videofile(output_path, fps=24)


