
import downloadVideo_curl
import os

count = 0


def track_output(number):
    out_count = number
    print(downloadVideo_curl.vid_list)
    for video_name in downloadVideo_curl.vid_list:
        # -t '1' 为track状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './track_output/{out_count}_output_video.mp4' -t '1'"
        os.system(shell)
        out_count += 1


def detect_output(number):
    out_count = number
    for video_name in downloadVideo_curl.vid_list:
        # -t '0' 为detect状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './detect_output/{out_count}_output_video.mp4' -t '0'"
        os.system(shell)
        out_count += 1


if __name__ == "__main__":
    downloadVideo_curl.download_tar(count)
    track_output(count)
    detect_output(count)
