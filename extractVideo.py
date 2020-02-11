#!/usr/local/bin/python3

import os


def tar_video(count, tar_list, video_list):

    video_list.clear
    vid_count = count

    for list in tar_list:

        tar_shell = f"tar -xzvf ./video_tar/{list} --strip-components 1 -C ./video_tar/Temp_video/"
        rmDS_shell = f"rm -rf ./video_tar/Temp_video/.DS_Store"
        rmTempVideo_shell = "rm -rf ./video_tar/Temp_video/*"

        os.system(tar_shell)
        os.system(rmDS_shell)
        tarVideo_list = os.listdir('./video_tar/Temp_video/')

        print(tarVideo_list)

        for tarVideo_name in tarVideo_list:
            rename_shell = f"mv ./video_tar/Temp_video/{tarVideo_name} ./video_mp4/{vid_count}_video.mp4"
            os.system(rename_shell)
            video_list.append(f"{vid_count}_video.mp4")
            vid_count += 1

        os.system(rmTempVideo_shell)

    print(video_list)
    return video_list
