<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>点赞插件 README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1 {
            color: #4CAF50;
        }
        h2 {
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-left: 5px solid #4CAF50;
            overflow-x: auto;
        }
        a {
            color: #4CAF50;
        }
        ul {
            margin: 0;
            padding: 0 0 0 20px;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>

<h1>点赞插件 README</h1>

<p>欢迎使用我们的点赞插件！该插件用于在蔷薇花园的聊天应用中，让用户进行点赞，从而提高互动体验。该插件依赖于 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的机器人框架</a>，具体信息如下。</p>

<h2>目录</h2>
<ul>
    <li><a href="#使用说明">使用说明</a></li>
    <li><a href="#功能说明">功能说明</a></li>
    <li><a href="#安装要求">安装要求</a></li>
    <li><a href="#配置">配置</a></li>
    <li><a href="#许可证">许可证</a></li>
    <li><a href="#致谢">致谢</a></li>
</ul>

<h2 id="使用说明">使用说明</h2>
<p>在使用插件之前，请务必进行以下两项注释操作，以确保插件正常运行：</p>
<ol>
    <li>在文件 <code>ws_iirose/transfer_plugin.py</code> 中，找到并注释以下行：
        <pre><code># user_leave_room(Message):  # 注释这一行</code></pre>
    </li>
    <li>在文件 <code>plugin/iirose_example.py</code> 中，找到并注释以下行：
        <pre><code># await API.like(Message.user_id)  # 触发进入房间后机器人会给触发的用户点赞  注释这一行</code></pre>
    </li>
</ol>

<h2 id="功能说明">功能说明</h2>
<p>该插件实现了如下功能：</p>
<ul>
    <li>用户可以通过发送“赞我”命令来进行点赞。</li>
    <li>每个用户每天只能点赞一次。</li>
    <li>点赞记录存储在一个 JSON 文件中。</li>
    <li>插件会反馈用户点赞是否成功。</li>
</ul>

<h2 id="安装要求">安装要求</h2>
<p>为了确保插件正常工作，请确保满足以下要求：</p>
<ul>
    <li><strong>Python 版本：</strong> <code>3.11</code></li>
    <li>安装以下库：
        <pre><code>pip install loguru</code></pre>
    </li>
</ul>
<p>该插件需要与 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的机器人框架</a> 一同使用。请确保您已正确安装并配置该框架。</p>

<h2 id="配置">配置</h2>
<p>插件依赖于一个 JSON 文件 <code>user_likes.json</code> 来存储点赞记录。运行插件时，如果文件不存在，插件将自动创建。</p>
<p>可以按照以下步骤配置点赞插件的默认备注信息：</p>
<ul>
    <li>更改 <code>DEFAULT_REMARK</code> 变量的值，以设置您希望的默认备注信息或图片 URL。
        <pre><code>DEFAULT_REMARK = "http://r.iirose.com/i/25/4/4/0/3223-JK.gif"  # 修改这一行</code></pre>
    </li>
</ul>

<h2 id="许可证">许可证</h2>
<p>该项目使用 <a href="LICENSE">MIT 许可证</a> 进行分发。</p>

<h2 id="致谢">致谢</h2>
<p>感谢使用本插件！如有任何问题或建议，请随时开 issue 或提出 PR。我们乐于接受反馈并不断改进。</p>
<p>如需查看更多信息或讨论，欢迎访问 <a href="https://github.com/XCWQW1/iirosebot">XCWQW233 的 GitHub 页面</a>！</p>

<p>希望你能享受使用这个插件！</p>

</body>
</html>
