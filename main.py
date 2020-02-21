
import downloadVideo_curl
import os

initCount = 0
downloadTar_list = []
downloadVid_list = []


def track_output(number, video_list):
    outVid_count = number
    for i in video_list:
        print('222222222+'+i)
    for video_name in video_list:
        print('3333333', video_name)
        # -t '1' 为track状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './track_output/{outVid_count}_output_video.mp4' -t '1'"
        os.system(shell)
        outVid_count += 1


def detect_output(number, video_list):
    outVid_count = number
    for video_name in video_list:
        # -t '0' 为detect状态
        shell = f"./track_test_ubuntu.out -i './video_mp4/{video_name}' -o './detect_output/{outVid_count}_output_video.mp4' -t '0'"
        os.system(shell)
        outVid_count += 1


if __name__ == "__main__":
    downloadVideo_curl.download_vid(initCount, downloadVid_list)
    track_output(initCount, downloadVid_list)
    detect_output(initCount, downloadVid_list)
