
import downloadVideo_curl
import os

initCount = 0


def track_output(number):
    outVid_count = number
    print(downloadVideo_curl.downloadVid_list)
    for video_name in downloadVideo_curl.downloadVid_list:
        # -t '1' 为track状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './track_output/{outVid_count}_output_video.mp4' -t '1'"
        os.system(shell)
        outVid_count += 1


def detect_output(number):
    outVid_count = number
    for video_name in downloadVideo_curl.downloadVid_list:
        # -t '0' 为detect状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './detect_output/{outVid_count}_output_video.mp4' -t '0'"
        os.system(shell)
        outVid_count += 1


if __name__ == "__main__":
    downloadVideo_curl.download_tar(initCount)
    track_output(initCount)
    detect_output(initCount)
