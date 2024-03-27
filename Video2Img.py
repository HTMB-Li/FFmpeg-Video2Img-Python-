import subprocess
import os


def extract_frames(video_path, output_dir):
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 调用FFmpeg命令
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', video_path,
        os.path.join(output_dir, 'frame_%04d.png')
    ]
    subprocess.run(ffmpeg_cmd)


if __name__ == "__main__":
    video_path = '视频文件路径'  # 视频文件路径
    output_dir = '输出帧的目录'  # 输出帧的目录
    extract_frames(video_path, output_dir)
