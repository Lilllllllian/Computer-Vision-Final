import json
import random
from pathlib import Path

# 输入输出路径
input_path = Path("transforms.json")
output_dir = input_path.parent

# 目标相机参数
camera_params = {
    "camera_angle_x": 0.2633031242076986,
    "camera_angle_y": 0.46239873986422275,
    "fl_x": 2718.6744390044205,
    "fl_y": 2718.6744390044205,
    "k1": 0.13851475357096796,
    "k2": 0,
    "k3": 0,
    "k4": 0,
    "p1": 0,
    "p2": 0,
    "is_fisheye": False,
    "cx": 360,
    "cy": 640,
    "w": 720,
    "h": 1280,
    "aabb_scale": 32
}

# 读取原始 transforms.json
with open(input_path, 'r') as f:
    data = json.load(f)

frames = data["frames"]
random.shuffle(frames)

# 按 5:1:4 分割
N = len(frames)
n_train = int(0.5 * N)
n_val = int(0.1 * N)
n_test = N - n_train - n_val

train_frames = frames[:n_train]
val_frames = frames[n_train:n_train + n_val]
test_frames = frames[n_train + n_val:]

# 构造写入函数
def write_split(filename, frames_subset):
    out_data = dict(camera_params)
    out_data["frames"] = frames_subset
    with open(output_dir / filename, 'w') as f:
        json.dump(out_data, f, indent=4)

# 写出三个 json 文件
write_split("transforms_train.json", train_frames)
write_split("transforms_val.json", val_frames)
write_split("transforms_test.json", test_frames)

print("transforms_train.json / val / test 写入成功~")
