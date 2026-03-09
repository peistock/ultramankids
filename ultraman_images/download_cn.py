import urllib.request
import ssl
import json
import re

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 百度百科的图片URL模式
baidu_baike_urls = {
    "阿古茹": "https://bkimg.cdn.bcebos.com/pic/42a98226cffc1e1706c89b724890f603728de9cd",
    "奈克瑟斯": "https://bkimg.cdn.bcebos.com/pic/3801213fb80e7bec54e7ac28252eb9389b506b90",
    "维克特利": "https://bkimg.cdn.bcebos.com/pic/9f510fb30f2442a7d933d2f79c43ad4bd113022f",
    "艾克斯": "https://bkimg.cdn.bcebos.com/pic/472309f790529822720e9189ce86bd6eddc438b2",
    "格丽乔": "https://bkimg.cdn.bcebos.com/pic/c75c10385343fbf2b211c9a19c3eca8064388fc5",
    "风马": "https://bkimg.cdn.bcebos.com/pic/b21c8701a18b87d6f72ac77f070828381f30fd15",
    "赛迦": "https://bkimg.cdn.bcebos.com/pic/30adcbef76094b3639d7db1daacc7cd98d109deb",
    "雷杰多": "https://bkimg.cdn.bcebos.com/pic/d62a6059252dd42a2834d251003b5bb5c9eab827",
    "迪迦": "https://bkimg.cdn.bcebos.com/pic/a5c27d1ed21b0ef41bd5c2b5d9c451da80cb3ef1",
}

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context, timeout=15) as response:
            if response.status == 200:
                data = response.read()
                if len(data) > 5000:
                    with open(filename, 'wb') as f:
                        f.write(data)
                    return True, len(data)
        return False, 0
    except Exception as e:
        return False, str(e)[:50]

# 下载图片
for name, url in baidu_baike_urls.items():
    filename = f"{name}.jpg"
    print(f"下载 {name} ...")
    success, info = download_image(url, filename)
    if success:
        print(f"  ✓ 成功 ({info} bytes)")
    else:
        print(f"  ✗ 失败: {info}")

print("\n完成!")
