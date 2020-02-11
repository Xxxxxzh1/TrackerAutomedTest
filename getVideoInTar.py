
import os


def tar_video(count, tar_list, video_list):

    vid_count = count

    for list in tar_list:
        # 解压固定层级文件至固定文件夹
        tar_shell = f"tar -xzvf ./video_tar/{list} --strip-components 1 -C ./video_tar/Temp_video/"
        rmDS_shell = f"rm -rf ./video_tar/Temp_video/.DS_Store"
        rmTempVideo_shell = "rm -rf ./video_tar/Temp_video/*"

        os.system(tar_shell)
        # 清除隐藏文件
        os.system(rmDS_shell)
        # 创建对应所有视频的列表
        tarVideo_list = os.listdir('./video_tar/Temp_video/')

        for tarVideo_name in tarVideo_list:
            rename_shell = f"mv ./video_tar/Temp_video/{tarVideo_name} ./video_mp4/{vid_count}_video.mp4"
            os.system(rename_shell)
            video_list.append(f"{vid_count}_video.mp4")
            vid_count += 1

        os.system(rmTempVideo_shell)

    return video_list
