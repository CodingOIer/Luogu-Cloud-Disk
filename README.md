# Luogu-Cloud-Disk 一个将洛谷云剪切板作为云盘的客户端

## 使用方法

### 配置文件

在编译后的程序同目录下编辑一个 `setting.json` 格式如下：

>  [!CAUTION]
>
> 如果不放置 `setting.json` 可能会有意想不到的结果。

```json
{
    "_uid": 123456,
    "//": "你的 uid (_uid)"
    "__client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    "//": "你的 cookie (__client_id)"
}
```

### 上传文件

运行编译后的程序，将任意文件直接拖入窗口即可，链接会自动复制到剪切板。

> [!NOTE]
>
> 由于洛谷的限制，文件最大约为 1MB。
>
> 请注意本程序可能会在你的云剪切板中创建非常长的内容，如果你对这方面有特殊的要求，请悉知。

### 下载文件

运行编译后的程序，将本程序制作的 url 粘贴即可，文件会放在同目录下，文件名与上传时相同。

> [!NOTE]
>
> 由于某些原因，访问他人的云剪切板需要跳转到洛谷国际，但访问速度极慢，我们目前并无对策。

> [!WARNING]
>
> 粘贴其他 url 可能会导致意想不到的结果。
>
> 可能会意外地覆盖文件。

## 储存格式

格式为 `filename?xxxxxxxxxxxxxxxxxxxx`，其中的 `?` 为英文右尖括号，`filename` 为上传时的文件名，`xxxxxxxxxxxxxxxxxxxx` 为二进制的 base64 编码。

## 自行构建

```shel
git clone https://github.com/CodingOIer/Luogu-Cloud-Disk
cd ./Luogu-Cloud-Disk
pip install ./requirements.txt
pyinstaller -icon logo.ico -F ./main.py
```