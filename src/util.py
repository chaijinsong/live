import re

def parse_lrc_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lrc_lines = f.readlines()
    
    lrc_dict = {}
    for line in lrc_lines:
        # 使用正则表达式匹配时间戳和歌词文本
        match = re.findall(r'\[(\d+):(\d+\.\d+)\](.*)', line)
        if match:
            # 将时间戳转换成浮点数
            timestamp = float(match[0][0]) * 60 + float(match[0][1])
            text = match[0][2].strip()
            lrc_dict[timestamp] = text

    return lrc_dict

def get_current_text(t, lrc_map):
    t = float(t)
    if (lrc_map.get(t)):
        return lrc_map.get(t) # 如果能直接找到，就用这个
    keys = list(lrc_map.keys())
    keys.sort()
    
    target = keys[0]
    for time in keys:
        if (time <= t):
            target = time
        else:
            return lrc_map.get(target)
    return lrc_map.get(target)
