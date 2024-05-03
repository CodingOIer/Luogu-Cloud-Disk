import requests
import urllib
import base64
import json
import pyperclip


_uid = 0
max_len = 1000000
__client_id = ''
cookie = ''


def init():
    global _uid, __client_id, cookie, max_len
    try:
        with open('./setting.json', 'r') as f:
            js = json.load(f)
        _uid = js['_uid']
        __client_id = js['__client_id']
        cookie = f'__client_id={__client_id}; _uid={_uid};'
        try:
            max_len = js['max_len']
        except:
            pass
        return True
    except:
        return False


def codeFile(file_path):
    with open(file_path, 'rb') as binary_file:
        binary_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_data)
        return base64_encoded_data.decode('utf-8')


def decodeFile(string_data, file_path):
    with open(file_path, 'wb') as binary_file:
        base64_decoded_data = base64.b64decode(string_data)
        binary_file.write(base64_decoded_data)


def rmb(s, t):
    index = s.find(t)
    if index == -1:
        return s
    return s[index + len(t) :]


def rma(s, t):
    index = s.find(t)
    if index == -1:
        return s
    return s[:index]


def getCsrfToken(url='https://www.luogu.com.cn'):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'x-luogu-type': 'content-only',
        'cookie': cookie,
        'x-requested-with': 'XMLHttpRequest',
    }
    res2 = requests.get(url, headers=headers)
    res2 = res2.text
    csrftoken = res2.split("<meta name=\"csrf-token\" content=\"")[-1].split("\">")[0]
    return csrftoken


def getHeaders(url='https://www.luogu.com.cn'):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cookie': cookie,
        'referer': 'https://www.luogu.com.cn/chat',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'x-csrf-token': getCsrfToken(url),
        'x-requested-with': 'XMLHttpRequest',
    }
    return headers


def getHeadersGet(url='https://www.luogu.com.cn'):
    headers = {
        'referer': url,
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }
    return headers


def decodeUrl(s):
    return urllib.parse.unquote(s)


def split(s):
    return [s[i:i+max_len] for i in range(0, len(s), max_len)]

def craftPaste(data):
    data = '```\nLuogu-Cloud-Disk\n' + data + '\n```'
    body = {
        'data': data,
        'public': True,
    }
    h = getHeaders()
    response = requests.post(
        'https://www.luogu.com.cn/paste/new',
        headers=h,
        json=body,
    )
    js = json.loads(response.text)
    return f'https://www.luogu.com.cn/paste/{js['id']}'

def getPaste(url):
    try:
        response = requests.get(
            url=url,
            headers=getHeadersGet('https://www.luogu.com.cn/paste'),
        )
        res = response.text
        res = rmb(res, 'JSON.parse(decodeURIComponent("')
        res = rma(res, '"));')
        js = json.loads(decodeUrl(res))
        data = js['currentData']['paste']['data']
        data = data[21:]
        data = data[:-4]
        return data
    except:
        pid = url.split('/')[-1]
        url = f'https://www.luogu.com/paste/{pid}'
        response = requests.get(
            url=url,
            headers=getHeadersGet('https://www.luogu.com.cn'),
        )
        res = response.text
        res = rmb(res, 'JSON.parse(decodeURIComponent("')
        res = rma(res, '"));')
        js = json.loads(decodeUrl(res))
        data =  js['currentData']['paste']['data']
        data = data[21:]
        data = data[:-4]
        return data

if __name__ == '__main__':
    if not init():
        _uid = 0
        __client_id = ''
        for _ in range(40):
            __client_id += '0'
    while True:
        filename = input("filename or url: ")
        if filename[:8] == '[REMOVE]':
            pid = ''
            for x in filename:
                pid += x
                if x == '/':
                    pid = ''
            url = f'https://www.luogu.com.cn/paste/{pid}'
            print(f'检测到为删除命令，开始删除主分片 {url}')
            data = getPaste(url)
            links = data.split('&')
            print(f'获取到 {len(links)} 个分片，开始删除')
            for l in links:
                kid = ''
                for x in l:
                    kid += x
                    if x == '/':
                        kid = ''
                print(f'正在删除第 {links.index(l)+1} 分片')
                response = requests.post(f'https://www.luogu.com.cn/paste/delete/{kid}', headers=getHeaders())
            print(f'删除完成，开始删除主分片')
            response = requests.post(f'https://www.luogu.com.cn/paste/delete/{pid}', headers=getHeaders())
            print('删除完成')
        elif filename[:5] == 'https':
            print('检测为主分片 url，开始下载')
            links = getPaste(filename)
            links = links.split('&')
            data = ''
            print(f'检测到 {len(links)} 个分片，开始下载')
            for l in links:
                print(f'正在下载第 {links.index(l)+1} 分片')
                data += getPaste(l)
            data = data.split('?')
            print('下载完成，开始解码')
            decodeFile(data[1], data[0])
            print(f'解码完成，文件已保存为 {data[0]}')
        else:
            print('检测到为文件路径，开始上传')
            if filename[0] == '"':
                filename = filename[1:]
            if filename[-1] == '"':
                filename = filename[:-1]
            code = codeFile(filename)
            name = ''
            for x in filename:
                name += x
                if x == '\\' or x == '/' or x == ':':
                    name = ''
            data = f'{name}?{code}'
            l = split(data)
            print(f'文件编码完成，开始上传，共分割为 {len(l)} 分片')
            links = ''
            for x in l:
                print(f'正在上传第 {l.index(x)+1} 分片')
                url = craftPaste(x)
                links += f'{url}&'
            links = links[:-1]
            print('上传完成，开始合成主分片')
            url = craftPaste(links)
            pyperclip.copy(url)
            print(f'上传成功，主分片已复制到剪切板，为 {url}')
        input('按回车继续')
        print('\033c', end='')
