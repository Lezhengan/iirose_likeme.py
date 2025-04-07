# 使用时请把  ws_iirose>transfer_plugin.py 中的 user_leave_room(Message):    使用#号注释
# 以及注释    plugin>iirose_example.py 中的 await API.like(Message.user_id)  # 触发进入房间后机器人会给触发的用户点赞  这一行注释

# 感谢使用！
import json
import os
from loguru import logger
from API.api_iirose import APIIirose
from API.decorator.command import on_command, MessageType
from datetime import datetime

API = APIIirose()



# 定义存储点赞记录的文件
LIKE_RECORD_FILE = 'user_likes.json'

# 初始化
if not os.path.exists(LIKE_RECORD_FILE):
    with open(LIKE_RECORD_FILE, 'w') as f:
        json.dump({}, f)  # 初始化为空字典

# 在这里设定你的默认自动备注图片或者信息
DEFAULT_REMARK = "http://r.iirose.com/i/25/4/4/0/3223-JK.gif"


# 注册“赞我”命令的处理函数
@on_command('赞我', False, command_type=[MessageType.room_chat, MessageType.private_chat])
async def send_like(Message):
    user_id = Message.user_id
    user_name = Message.user_name or "用户"

    # 读取当前点赞记录
    with open(LIKE_RECORD_FILE, 'r') as f:
        user_likes = json.load(f)

    # 获取今日日期字符串
    today = datetime.now().strftime("%Y-%m-%d")

    # 检查用户是否今天已经点赞
    if user_likes.get(user_id) == today:
        await API.send_msg(Message, f" [*{user_name}*] ，您今天已经点赞过了！")
        return

    try:
        # 使用位置参数调用点赞
        response = await API.like(user_id, DEFAULT_REMARK)  # 传入用户 ID 和固定的备注

        # 判断点赞是否成功
        if response.get("code") == 200:
            # 更新点赞记录
            user_likes[user_id] = today
            with open(LIKE_RECORD_FILE, 'w') as f:
                json.dump(user_likes, f)  # 更新记录到文件

            # 返回点赞成功的信息和用户提供的图片 URL
            image_url = Message.message
            await API.send_msg(Message, f"已成功点赞！")
        else:
            await API.send_msg(Message, "点赞失败，请稍后再试。")

    except Exception as e:
        logger.error(f"点赞过程中发生错误：{str(e)}")
        await API.send_msg(Message, "点赞失败，请稍后再试。")
