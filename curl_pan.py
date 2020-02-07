#!/usr/local/bin/python3

import video_sharelink
import os

# count = 0
vid_list = []
tar_list = []


def download_tar(number):
    list_count = number
    tar_list.clear
    os.system('rm -rf ./video_tar/*')

    for url in video_sharelink.folder_sharelink:
        shell = f"curl -J -0 {url}/download --output ./video_tar/{list_count}_video.tar"
        os.system(shell)
        tar_list.append(f"{list_count}_video.tar")
        list_count += 1


def download_vid(number):
    list_count = number
    os.system('rm -rf ./video_mp4/*')
    vid_list.clear
    for url in video_sharelink.video_sharelink:
        shell = f"curl -J -0 {url}/download --output ./video_mp4/{list_count}_video.mp4"
        os.system(shell)
        vid_list.append(f"{list_count}_video.mp4")
        list_count += 1


# if __name__ == "__main__":
#     download_vid(count)
#     print('视频拉取完毕')
