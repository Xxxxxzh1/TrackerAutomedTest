
import downloadVideo_curl
import os

initCount = 0
downloadZip_list = []
downloadVid_list = []


def track_output(number, video_list):
    outVid_count = number
    os.system("rm -rf ./track_output/*")
    for video_name in video_list:
        # -t '1' 为track状态
        shell = f"../Tracker/build/track_example -i './video_mp4/{video_name}' -o './track_output/{outVid_count}_output_video.mp4'"
        os.system(shell)
        outVid_count += 1


def detect_output(number, video_list):
    outVid_count = number
    os.system("rm -rf ./detect_output/*")
    for video_name in video_list:
        # -t '0' 为detect状态
        shell = f"../Tracker/build/track_example -i './video_mp4/{video_name}' -o './detect_output/{outVid_count}_output_video.mp4'"
        os.system(shell)
        outVid_count += 1


if __name__ == "__main__":
    # downloadVideo_curl.download_zip(initCount, downloadZip_list, downloadVid_list)
    # print('after download vid_list: ', downloadVid_list)
    downloadVideo_curl.download_vid(initCount, downloadVid_list)
    # track_output(initCount, downloadVid_list)
    detect_output(initCount, downloadVid_list)
