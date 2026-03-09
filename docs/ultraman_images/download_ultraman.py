import urllib.request
import urllib.parse
import ssl
import os

# 创建SSL上下文，忽略证书验证
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 定义每个奥特曼的图片URL（从可靠来源）
ultraman_images = {
    "阿古茹": [
        "https://upload.wikimedia.org/wikipedia/en/9/9d/Ultraman_Agul.png",
        "https://static.wikia.nocookie.net/ultra/images/8/8a/Ultraman_Agul_V2.png",
        "https://www.ultramanwiki.com/images/Agul_V2.jpg",
    ],
    "奈克瑟斯": [
        "https://upload.wikimedia.org/wikipedia/en/3/3a/Ultraman_Nexus_Junis.png",
        "https://static.wikia.nocookie.net/ultra/images/9/9a/Ultraman_Nexus_Junis.png",
        "https://www.ultramanwiki.com/images/Nexus_Junis.jpg",
    ],
    "维克特利": [
        "https://upload.wikimedia.org/wikipedia/en/8/8e/Ultraman_Victory.png",
        "https://static.wikia.nocookie.net/ultra/images/b/b0/Ultraman_Victory.png",
        "https://www.ultramanwiki.com/images/Victory.jpg",
    ],
    "艾克斯": [
        "https://upload.wikimedia.org/wikipedia/en/7/7a/Ultraman_X.png",
        "https://static.wikia.nocookie.net/ultra/images/8/8e/Ultraman_X.png",
        "https://www.ultramanwiki.com/images/X.jpg",
    ],
    "格丽乔": [
        "https://upload.wikimedia.org/wikipedia/en/a/a0/Ultrawoman_Grigio.png",
        "https://static.wikia.nocookie.net/ultra/images/3/3c/Ultrawoman_Grigio.png",
        "https://www.ultramanwiki.com/images/Grigio.jpg",
    ],
    "风马": [
        "https://upload.wikimedia.org/wikipedia/en/4/4e/Ultraman_Fuma.png",
        "https://static.wikia.nocookie.net/ultra/images/9/9e/Ultraman_Fuma.png",
        "https://www.ultramanwiki.com/images/Fuma.jpg",
    ],
    "赛迦": [
        "https://upload.wikimedia.org/wikipedia/en/1/1a/Ultraman_Saga.png",
        "https://static.wikia.nocookie.net/ultra/images/8/8a/Ultraman_Saga.png",
        "https://www.ultramanwiki.com/images/Saga.jpg",
    ],
    "雷杰多": [
        "https://upload.wikimedia.org/wikipedia/en/5/5e/Ultraman_Legend.png",
        "https://static.wikia.nocookie.net/ultra/images/7/7a/Ultraman_Legend.png",
        "https://www.ultramanwiki.com/images/Legend.jpg",
    ],
    "迪迦": [
        "https://upload.wikimedia.org/wikipedia/en/9/9a/Ultraman_Tiga.png",
        "https://static.wikia.nocookie.net/ultra/images/8/8e/Ultraman_Tiga_Multi_Type.png",
        "https://www.ultramanwiki.com/images/Tiga_Multi.jpg",
    ]
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            if response.status == 200:
                data = response.read()
                if len(data) > 1000:  # 确保不是错误页面
                    with open(filename, 'wb') as f:
                        f.write(data)
                    return True, len(data)
        return False, 0
    except Exception as e:
        return False, str(e)

# 下载每个奥特曼的图片
for name, urls in ultraman_images.items():
    filename = f"{name}.jpg"
    print(f"\n下载 {name} 奥特曼...")
    
    success = False
    for url in urls:
        success, info = download_image(url, filename)
        if success:
            print(f"  ✓ 成功下载: {filename} ({info} bytes)")
            break
        else:
            print(f"  ✗ 失败: {url[:60]}... - {info}")
    
    if not success:
        print(f"  ✗ 所有来源都失败，需要手动下载 {name}")

print("\n下载完成！")
