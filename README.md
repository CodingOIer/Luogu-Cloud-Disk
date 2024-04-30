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
    "__client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "//": "你的 cookie (__client_id)"
    "max_len": 1000000,
    "//": "每个子分片最大大小，建议默认"
}
```

### 上传文件

运行编译后的程序，将任意文件直接拖入窗口即可，主分片链接会自动复制到剪切板。

> [!NOTE]
>
> 由于洛谷的限制，文件会自动切分为分片。
>
> 上传文件后建议不要打开云剪切板界面，否则可能会导致浏览器失去响应。
>
> 如果文件非常大，其可能创建极多且极大的云剪切板，可能对洛谷性能造成一定影响，请考虑下文的「删除分片」。

### 下载文件

运行编译后的程序，将本程序制作的主分片 url 粘贴即可，文件会放在同目录下，文件名与上传时相同。

> [!NOTE]
>
> 由于某些原因，访问他人的云剪切板需要跳转到洛谷国际，但访问速度极慢，我们目前并无对策。

> [!WARNING]
>
> 粘贴其他 url 可能会导致意想不到的结果。
>
> 如果文件重名，可能会意外地覆盖文件。

### 删除分片

运行编译后的程序，将本程序制作的**主分片** url 下面格式输入。

```shell
[REMOVE] https://www.luogu.com.cn/xxxxxxxx
```

请严格按照此格式，注意空格，以及必须是 `.com.cn` 域名。

> [!CAUTION]
>
> 本功能测试中，如果导致其他云剪切板被误删除等灾难性后果请自行承担。

## 储存格式

每隔剪切板会使用代码段包裹数据，代码段第一行为 `Luogu-Cloud-Disk`。

将所有分片合并后的格式为 `filename?xxxxxxxxxxxxxxxxxxxx`，其中的 `?` 为英文右尖括号，`filename` 为上传时的文件名，`xxxxxxxxxxxxxxxxxxxx` 为二进制的 base64 编码。

## 自行构建

```shel
git clone https://github.com/CodingOIer/Luogu-Cloud-Disk
cd ./Luogu-Cloud-Disk
pip install ./requirements.txt
pyinstaller -icon logo.ico -F ./main.py
```