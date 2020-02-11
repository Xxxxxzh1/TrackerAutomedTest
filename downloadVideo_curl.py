
import video_sharelink
import os
import extractVideo

vid_list = []
tar_list = []


def download_tar(count):
    list_count = count
    tar_list.clear
    vid_list.clear
    os.system('rm -rf ./video_tar/*')

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.folder_sharelink:
        shell = f"curl -J -0 {url}/download --output ./video_tar/{list_count}_video.tar"
        os.system(shell)
        tar_list.append(f"{list_count}_video.tar")
        list_count += 1

    # 调用函数解压当前所有压缩文件
    extractVideo.tar_video(count, tar_list, vid_list)


def download_vid(count):
    list_count = count
    os.system('rm -rf ./video_mp4/*')
    vid_list.clear

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.video_sharelink:
        shell = f"curl -J -0 {url}/download --output ./video_mp4/{list_count}_video.mp4"
        os.system(shell)
        vid_list.append(f"{list_count}_video.mp4")
        list_count += 1
