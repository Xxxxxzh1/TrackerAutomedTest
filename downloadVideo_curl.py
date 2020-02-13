
import video_sharelink
import os
import extractVideo

downloadTar_list = []
downloadVid_list = []


def download_tar(count):
    list_count = count
    downloadTar_list.clear
    downloadVid_list.clear
    os.system('rm -rf ./video_tar/*')
    os.system('mkdir ./video_tar/Temp_video')

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.folder_sharelink:
        downloadTar_shell = f"curl -J -0 {url}/download --output ./video_tar/{list_count}_video.tar"
        os.system(downloadTar_shell)
        downloadTar_list.append(f"{list_count}_video.tar")
        list_count += 1

    print(downloadTar_list)
    # 调用函数解压当前所有压缩文件
    extractVideo.getVdieo(count, downloadTar_list, downloadVid_list)


def download_vid(count):
    list_count = count
    os.system('rm -rf ./video_mp4/*')
    downloadVid_list.clear

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.video_sharelink:
        downloadVid_shell = f"curl -J -0 {url}/download --output ./video_mp4/{list_count}_video.mp4"
        os.system(downloadVid_shell)
        downloadVid_list.append(f"{list_count}_video.mp4")
        list_count += 1
