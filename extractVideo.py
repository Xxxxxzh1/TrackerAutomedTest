
import os


def getVideo(count, zip_list, video_list):

    vid_count = count

    print('recieve information: ', count, zip_list, video_list)

    for zipName in zip_list:

        extractZip_shell = f"unzip ./video_zip/{zipName} -d './video_zip/Temp_video' && mv './video_zip/Temp_video'/*/* './video_zip/Temp_video/' && rmdir ./video_zip/Temp_video/*"
        rmDS_shell = f"rm -rf ./video_zip/Temp_video/.DS_Store"

        # 提取压缩包次级文件夹下的所有视频至/Temp_video/路径下
        os.system(extractZip_shell)

        os.system(rmDS_shell)
        # 得到当前压缩包所有视频名称列表
        videoInZip_list = os.listdir('./video_zip/Temp_video/')
        print('video in zip: ', videoInZip_list)

        for videoInZip_name in videoInZip_list:
            print('every pre_video name: ', videoInZip_name)
            rename_shell = f"mv ./video_zip/Temp_video/{videoInZip_name} ./video_mp4/{vid_count}_video.mp4"
            # 给解压得到的视频重命名并移至/video_mp4/路径
            os.system(rename_shell)
            video_list.append(f"{vid_count}_video.mp4")
            vid_count += 1
        os.system('rm -rf ./video_zip/Temp_video')
    print('video_list: ', video_list)
