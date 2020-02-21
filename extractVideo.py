
import os


def getVdieo(count, tar_list, video_list):

    vid_count = count

    for tarName in tar_list:

        tar_shell = f"tar -xzvf ./video_tar/{tarName} --strip-components 1 -C ./video_tar/Temp_video/"
        rmDS_shell = f"rm -rf ./video_tar/Temp_video/.DS_Store"

        # 提取压缩包次级文件夹下的所有视频至/Temp_video/路径下
        os.system(tar_shell)

        os.system(rmDS_shell)
        # 得到当前压缩包所有视频名称列表
        videoInTar_list = os.listdir('./video_tar/Temp_video/')

        for videoInTar_name in videoInTar_list:
            rename_shell = f"mv ./video_tar/Temp_video/{videoInTar_name} ./video_mp4/{vid_count}_video.mp4"
            # 给解压得到的视频重命名并移至/video_mp4/路径
            os.system(rename_shell)

            video_list.append(f"{vid_count}_video.mp4")
            vid_count += 1
    print('video in tar: ', video_list)
