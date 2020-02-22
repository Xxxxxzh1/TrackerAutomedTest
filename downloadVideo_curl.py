
import video_sharelink
import os
import extractVideo


def download_zip(count, zip_list, video_list):
    zipList_count = count
    zip_list.clear
    video_list.clear
    os.system("rm -rf ./video_mp4/*")
    os.system("rm -rf ./video_zip/*")
    # os.system("mkdir ./video_zip/Temp_video")

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.folder_sharelink:
        downloadZip_shell = f"curl -J -0 {url}/download --output ./video_zip/{zipList_count}_video.zip"
        os.system(downloadZip_shell)
        zip_list.append(f"{zipList_count}_video.zip")
        zipList_count += 1

    # print('current zip_list: ', zip_list)
    # 调用函数解压当前所有压缩文件
    extractVideo.getVideo(count, zip_list, video_list)


def download_vid(count, video_list):
    list_count = count
    os.system("rm -rf ./video_mp4/*")
    video_list.clear

    # 按link中的链接下载所有压缩包
    for url in video_sharelink.video_sharelink:
        downloadVid_shell = f"curl -J -0 {url}/download --output ./video_mp4/{list_count}_video.mp4"
        os.system(downloadVid_shell)
        video_list.append(f"{list_count}_video.mp4")
        list_count += 1
