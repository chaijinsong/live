

视频文件地址：/Users/didi/Desktop/LiveStream/source/noSee.mkv
推流拉流地址：rtmp://live-push.bilivideo.com/live-bvc/?streamname=live_329635520_8991473&key=07a50f4a4e00721b01f06b914171de2e&schedule=rtmp&pflag=1
acc：RTMP的音频格式
flv： RTMP的视频格式

ffmpeg -re -i /Users/didi/Desktop/LiveStream/source/xs_fs.flac -preset ultrafast -vcodec libx264 -acodec aac -f flv "rtmp://live-push.bilivideo.com/live-bvc/?streamname=live_329635520_8991473&key=07a50f4a4e00721b01f06b914171de2e&schedule=rtmp&pflag=1"



ffmpeg -re -i /home/lighthouse/bilibili/movies/test1.mp4 -preset ultrafast -vcodec libx264 -g 60 -b:v 1500k -c:a aac -b:a 92k -strict -2 -f flv "rtmp://live-push.bilivideo.com/live-bvc/?streamname=live_329635520_8991473&key=07a50f4a4e00721b01f06b914171de2e&schedule=rtmp&pflag=1"


腾讯云IP：101.42.42.254
腾讯云轻量服务器密码：CjS@15035806407


wget --no-check-certificate https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.4.1-i686-static.tar.xz
