Description
====
- 采用可执行文件 .out 对视频文件做track/detect处理
- 依赖：OS
- 在Python3环境运行main.py
- video_sharelink.py中的链接配置了两套参数，video_sharelink为输入视频的网盘分享链接，folder_sharelink为输入视频在网盘所在文件夹分享链接（方便批量输入）
- CI轮询通过监听是否有新的提交（包括链接的更改、编译出tracker网络的二进制文件）

History
====
- 20200210:
更改 ubuntu18-tracker-autorun 服务器上的执行文件为track_test_ubuntu.out

- 20200211:
增加对视频文件夹链接的读取--解压--输出视频功能