##Tracker自动化接口定义
###Detecting
- 接口定义
    - 输入：
input_video_path--本地视频的绝对路径<br/>
![-w365](media/15790133867398.jpg)

    - 输出：
output_video--算法网络处理后的视频
视频中每一帧需要对可识别的目标标示特定的符号（如在识别目标的中心点以绿圈显示）<br/>
output_log--按帧记录的结果log
每一帧的序列号
每一帧的时间戳 
每一帧可识别的目标总数
每个可识别目标的位置信息（以视频左下角为原点，建立一个单位坐标系，以X/Y标示位置）<br/>
![-w459](media/15790145470037.jpg)


***

###Tracking
- 接口定义
    - 输入：
    input_video_path--本地视频的相对路径
    input_target_coord--选定目标的位置
    input_frame_seq--选定目标对应帧的起始/结束序列号<br/>
    ![-w377](media/15790139447776.jpg)

    - 输出：
    output_video--算法网络处理后的视频
    视频中对序列号为 start_seq 的帧做锁定目标处理,锁定目标为离 input_target_coord 直线距离最近的那一个，用特定标识给出（如 BoundingBox ），直至帧序列号为 end_seq 结束锁定处理。在 start_seq：end_seq 之外的序列帧按 detecting 接口处理。<br/>
    output_log--按帧记录的结果log
    每一帧的序列号
    每一帧的时间戳 
    每一帧可识别的目标总数
    每个可识别目标的位置信息（以视频左下角为原点，建立一个单位坐标系，以X/Y标示位置）
    每个目标是否被锁定的布尔值<br/>
    ![-w460](media/15790150769048.jpg)
