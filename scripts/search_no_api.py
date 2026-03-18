#!/usr/bin/env python3
"""
免 API Key 搜索工具

通过直接抓取搜索引擎结果页实现搜索，无需 Brave API Key。
支持必应中国、百度、搜狗等中文搜索引擎。

使用方法:
    python search_no_api.py "搜索关键词" [引擎]
    
示例:
    python search_no_api.py "多莉斯 公众号"
    python search_no_api.py "AI 新闻" bing
    python search_no_api.py "Python 教程" baidu
"""

import sys
import urllib.parse
from pathlib import Path

# 颜色输出
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def get_search_url(query, engine='bing'):
    """获取搜索引擎 URL"""
    encoded_query = urllib.parse.quote(query, safe='')
    
    engines = {
        'bing': f"https://cn.bing.com/search?q={encoded_query}",
        'baidu': f"https://www.baidu.com/s?wd={encoded_query}",
        'sogo': f"https://www.sogou.com/web?query={encoded_query}",
        'google': f"https://www.google.com/search?q={encoded_query}&hl=zh-CN",
        'google-hk': f"https://www.google.com.hk/search?q={encoded_query}&hl=zh-CN"
    }
    
    return engines.get(engine, engines['bing'])

def print_usage():
    """打印使用说明"""
    print(f"""
{Colors.BOLD}免 API Key 搜索工具{Colors.END}

{Colors.CYAN}用法:{Colors.END}
    python search_no_api.py "搜索关键词" [引擎]

{Colors.CYAN}支持的引擎:{Colors.END}
    bing     - 必应中国（推荐）
    google   - Google（结果更全面）
    google-hk- Google 香港（中文结果好）
    baidu    - 百度
    sogo     - 搜狗

{Colors.CYAN}示例:{Colors.END}
    python search_no_api.py "多莉斯 公众号"
    python search_no_api.py "AI 新闻" bing
    python search_no_api.py "Python 教程" google
    python search_no_api.py "营销案例" google-hk

{Colors.CYAN}在 OpenClaw 中直接使用:{Colors.END}
    必应：web_fetch(url="https://cn.bing.com/search?q=多莉斯 + 公众号", extractMode="markdown")
    Google: web_fetch(url="https://www.google.com/search?q=多莉斯 + 营销&hl=zh-CN", extractMode="markdown")
    Google 香港：web_fetch(url="https://www.google.com.hk/search?q=多莉斯 + 营销&hl=zh-CN", extractMode="markdown")
""")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        return
    
    query = sys.argv[1]
    engine = sys.argv[2] if len(sys.argv) > 2 else 'bing'
    
    print_header("免 API Key 搜索工具")
    
    print(f"{Colors.BOLD}搜索关键词:{Colors.END} {query}")
    print(f"{Colors.BOLD}搜索引擎:{Colors.END} {engine}\n")
    
    # 生成搜索 URL
    search_url = get_search_url(query, engine)
    
    print(f"{Colors.CYAN}搜索链接:{Colors.END}")
    print(f"  {search_url}\n")
    
    print(f"{Colors.CYAN}在 OpenClaw 中使用以下命令:{Colors.END}")
    print(f"  web_fetch(url=\"{search_url}\", extractMode=\"markdown\")\n")
    
    print(f"{Colors.YELLOW}注意:{Colors.END}")
    print("  1. 直接点击链接可在浏览器查看结果")
    print("  2. 在 OpenClaw 中用 web_fetch 抓取结果页")
    print("  3. 频繁搜索可能被限流，建议间隔 5-10 秒")
    print()
    
    # 生成常用搜索命令
    print_header("快速命令")
    
    queries = {
        "微信公众号": f"web_fetch(url=\"https://cn.bing.com/search?q={urllib.parse.quote(query + ' 公众号', safe='')}\", extractMode=\"markdown\")",
        "知乎内容": f"web_fetch(url=\"https://cn.bing.com/search?q={urllib.parse.quote(query + ' site:zhihu.com', safe='')}\", extractMode=\"markdown\")",
        "最新内容": f"web_fetch(url=\"https://cn.bing.com/search?q={urllib.parse.quote(query, safe='')}&freshness=week\", extractMode=\"markdown\")",
    }
    
    for name, cmd in queries.items():
        print(f"{Colors.GREEN}{name}:{Colors.END}")
        print(f"  {cmd}\n")

if __name__ == "__main__":
    main()
