# 点赞插件 README

欢迎使用我们的点赞插件！该插件用于在蔷薇花园的聊天应用中，让用户进行点赞，从而提高互动体验。该插件依赖于 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的机器人框架</a>，具体信息如下。

## 目录

- [使用说明](#使用说明)
- [功能说明](#功能说明)
- [安装要求](#安装要求)
- [配置](#配置)
- [许可证](#许可证)
- [致谢](#致谢)

## 使用说明

在使用插件之前，请务必进行以下两项注释操作，以确保插件正常运行：

1. 在文件 `<code>ws_iirose/transfer_plugin.py</code>` 中，找到并注释以下行：
   <pre><code># user_leave_room(Message):  # 注释这一行</code></pre>

2. 在文件 `<code>plugin/iirose_example.py</code>` 中，找到并注释以下行：
   <pre><code># await API.like(Message.user_id)  # 触发进入房间后机器人会给触发的用户点赞  注释这一行</code></pre>

## 功能说明

该插件实现了如下功能：
- 用户可以通过发送“赞我”命令来进行点赞。
- 每个用户每天只能点赞一次。
- 点赞记录存储在一个 JSON 文件中。
- 插件会反馈用户点赞是否成功。

## 安装要求

为了确保插件正常工作，请确保满足以下要求：

- **Python 版本**：**3.11**
- 安装以下库：
   <pre><code>pip install loguru</code></pre>

该插件需要与 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的机器人框架</a> 一同使用。请确保您已正确安装并配置该框架。

## 配置

插件依赖于一个 JSON 文件 `<code>user_likes.json</code>` 来存储点赞记录。运行插件时，如果文件不存在，插件将自动创建。

可以按照以下步骤配置点赞插件的默认备注信息：

- 更改 `<code>DEFAULT_REMARK</code>` 变量的值，以设置您希望的默认备注信息或图片 URL：
   <pre><code>DEFAULT_REMARK = "http://r.iirose.com/i/25/4/4/0/3223-JK.gif"  # 修改这一行</code></pre>

## 许可证

该项目使用 <a href="LICENSE">MIT 许可证</a> 进行分发。

## 致谢

感谢使用本插件！如有任何问题或建议，请随时开 issue 或提出 PR。我们乐于接受反馈并不断改进。

如需查看更多信息或讨论，欢迎访问 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的 GitHub 页面</a>！

希望你能享受使用这个插件！
