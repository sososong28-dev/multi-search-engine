#!/usr/bin/env python3
"""
Multi-Search-Engine 示例脚本

演示如何使用 OpenClaw 的 web_search 和 web_fetch 工具进行搜索。
此脚本仅供参考，实际搜索由 OpenClaw 工具直接处理。

使用方法:
    python search_example.py "搜索关键词"
"""

import sys
import json

def print_search_tips():
    """打印搜索技巧"""
    tips = """
╔══════════════════════════════════════════════════════════╗
║           Multi-Search-Engine 搜索技巧                   ║
╠══════════════════════════════════════════════════════════╣
║  1. 精确搜索：用引号包裹关键词 "精确匹配"                ║
║  2. 排除词汇：用 - 排除不需要的内容 苹果 -手机           ║
║  3. 站内搜索：site:github.com 关键词                     ║
║  4. 文件类型：filetype:pdf 关键词                        ║
║  5. 时间过滤：freshness="week" 获取一周内内容            ║
║  6. 多引擎：当前使用 Brave Search，支持 Google/Bing 索引 ║
╚══════════════════════════════════════════════════════════╝
    """
    print(tips)

def main():
    if len(sys.argv) < 2:
        print("用法：python search_example.py \"搜索关键词\"")
        print("\n示例:")
        print('  python search_example.py "AI 最新进展"')
        print('  python search_example.py "Python 教程"')
        print_search_tips()
        return
    
    query = sys.argv[1]
    print(f"\n🔍 搜索查询：{query}")
    print("\n在 OpenClaw 中，你可以直接说:")
    print(f'  "帮我搜索一下 {query}"')
    print("\n我会自动使用 web_search 工具进行搜索！")
    print_search_tips()

if __name__ == "__main__":
    main()
