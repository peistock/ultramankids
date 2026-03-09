#!/usr/bin/env python3
"""
奥特曼图片下载助手
使用方法：
1. 安装依赖: pip install requests
2. 运行: python3 下载奥特曼图片.py
3. 下载完成后刷新网页即可看到图片
"""

import os
import requests
from urllib.parse import quote

# 创建图片目录
os.makedirs('ultraman_images', exist_ok=True)

# 奥特曼列表（按分类）
ultraman_list = {
    "昭和系": ["初代", "赛文", "杰克", "艾斯", "泰罗", "雷欧", "爱迪"],
    "平成系": ["迪迦", "戴拿", "盖亚", "阿古茹", "高斯", "奈克瑟斯", "麦克斯", "梦比优斯"],
    "新生代": ["赛罗", "银河", "维克特利", "艾克斯", "欧布", "捷德", "罗索", "布鲁", "格丽乔", "泰迦", "泰塔斯", "风马"],
    "令和系": ["泽塔", "特利迦", "德凯", "布莱泽", "亚刻"],
    "特殊": ["赛迦", "雷杰多", "诺亚", "奥特之王"]
}

# 尝试下载图片的函数
def download_image(name, category):
    """尝试从多个源下载奥特曼图片"""
    
    # 搜索关键词
    search_name = f"{name}奥特曼"
    
    # 文件名
    filename = f"ultraman_images/{name}.jpg"
    
    # 如果已存在，跳过
    if os.path.exists(filename):
        print(f"✓ {name}.jpg 已存在，跳过")
        return True
    
    print(f"尝试下载: {search_name}...", end=" ")
    
    # 这里使用占位方式，因为真实的图片下载需要具体的URL
    # 你可以在这里添加真实的图片URL
    
    # 尝试使用维基百科或其他源
    # 注意：由于版权和链接稳定性问题，这里只是示例
    
    print("请手动下载")
    return False

# 主函数
def main():
    print("=" * 50)
    print("奥特曼图片下载助手")
    print("=" * 50)
    print()
    
    total = 0
    success = 0
    
    for category, names in ultraman_list.items():
        print(f"\n【{category}】")
        for name in names:
            total += 1
            if download_image(name, category):
                success += 1
    
    print()
    print("=" * 50)
    print(f"总计: {total} 张图片")
    print(f"已有: {success} 张")
    print(f"需下载: {total - success} 张")
    print("=" * 50)
    print()
    print("由于网络图片的防盗链限制，建议手动下载：")
    print("1. 打开百度图片 (image.baidu.com)")
    print("2. 搜索'奥特曼名字 官方'，如'迪迦奥特曼 官方'")
    print("3. 找到喜欢的图片，右键保存到 ultraman_images 文件夹")
    print("4. 命名为: 初代.jpg, 赛罗.jpg 等（或 初代奥特曼.jpg）")
    print()
    print("支持的命名格式：")
    print("- 初代.jpg 或 初代奥特曼.jpg")
    print("- 赛罗.jpg 或 赛罗奥特曼.jpg")
    print()
    print("下载完成后刷新网页即可看到真实图片！")

if __name__ == "__main__":
    main()
