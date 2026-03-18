#!/usr/bin/env python3
"""
Multi-Search-Engine 测试脚本

用于验证搜索功能配置是否正确，测试中文搜索效果。

使用方法:
    python test_search.py [--api-key YOUR_KEY]
"""

import os
import sys
import json
from pathlib import Path

# 颜色输出
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def check_api_key():
    """检查 API key 是否配置"""
    print_header("步骤 1: 检查 API Key 配置")
    
    api_key = os.environ.get('BRAVE_API_KEY')
    
    if api_key:
        print_success(f"API Key 已配置 (末尾：...{api_key[-4:] if len(api_key) > 4 else api_key})")
        return True
    else:
        print_error("API Key 未配置")
        print_warning("\n配置方法:")
        print("  1. 运行命令：openclaw configure --section web")
        print("  2. 或设置环境变量：BRAVE_API_KEY=your_key")
        return False

def check_skill_files():
    """检查技能文件是否完整"""
    print_header("步骤 2: 检查技能文件")
    
    skill_dir = Path(__file__).parent.parent
    required_files = [
        'SKILL.md',
        'package.json',
        'references/search-config.json',
        'references/README.md',
        'references/quick-reference.md',
        'scripts/search_example.py'
    ]
    
    all_exist = True
    for file in required_files:
        file_path = skill_dir / file
        if file_path.exists():
            print_success(f"{file} 存在")
        else:
            print_error(f"{file} 缺失")
            all_exist = False
    
    return all_exist

def check_search_config():
    """检查搜索配置文件"""
    print_header("步骤 3: 检查搜索配置")
    
    config_path = Path(__file__).parent.parent / 'references' / 'search-config.json'
    
    if not config_path.exists():
        print_error("search-config.json 不存在")
        return False
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print_success("配置文件格式正确")
        
        # 检查必要字段
        if config.get('defaultEngine'):
            print_success(f"默认引擎：{config['defaultEngine']}")
        else:
            print_warning("未设置 defaultEngine")
        
        if config.get('forceChinese'):
            print_success("已启用强制中文模式")
        else:
            print_warning("未启用强制中文模式")
        
        engines = config.get('engines', {})
        if engines:
            print_success(f"配置了 {len(engines)} 个搜索引擎")
            for name, info in engines.items():
                print(f"  - {name}: {info.get('name', 'Unknown')}")
        
        return True
        
    except json.JSONDecodeError as e:
        print_error(f"配置文件格式错误：{e}")
        return False

def show_test_commands():
    """显示测试命令"""
    print_header("步骤 4: 测试搜索功能")
    
    print("在 OpenClaw 中运行以下命令测试搜索：\n")
    
    tests = [
        ("基础中文搜索", 'web_search(query="AI 新闻", country="CN", language="zh", search_lang="zh-hans", count=5)'),
        ("微信公众号搜索", 'web_search(query="多莉斯 公众号", country="CN", language="zh", search_lang="zh-hans")'),
        ("最新新闻（24h）", 'web_search(query="科技新闻", freshness="day", country="CN", language="zh", count=5)'),
        ("知乎内容搜索", 'web_search(query="Python 教程 site:zhihu.com", country="CN", language="zh", count=5)'),
    ]
    
    for i, (name, cmd) in enumerate(tests, 1):
        print(f"{Colors.BOLD}测试 {i}: {name}{Colors.END}")
        print(f"  {cmd}\n")
    
    print_warning("如果提示 missing_brave_api_key，请先配置 API Key")

def main():
    print(f"\n{Colors.BOLD}╔════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BOLD}║     Multi-Search-Engine 技能配置检查工具                ║{Colors.END}")
    print(f"{Colors.BOLD}╚════════════════════════════════════════════════════════╝{Colors.END}\n")
    
    # 执行检查
    api_key_ok = check_api_key()
    files_ok = check_skill_files()
    config_ok = check_search_config()
    
    # 显示测试命令
    show_test_commands()
    
    # 总结
    print_header("检查总结")
    
    if api_key_ok and files_ok and config_ok:
        print_success("所有检查通过！技能已就绪！🎉")
        print("\n下一步：运行测试搜索命令验证功能")
    else:
        print_warning("部分检查未通过，请根据上述提示修复")
        if not api_key_ok:
            print("\n优先配置 API Key，否则无法使用搜索功能")
    
    print()

if __name__ == "__main__":
    main()
