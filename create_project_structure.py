# -*- coding: utf-8 -*-
"""
Created on ${DATE}
@author: YourName
Description:
create_project_structure.py
用途：自动生成标准项目目录结构和预配置的.gitignore文件
"""

import os
from pathlib import Path

# 基础目录结构配置
PROJECT_STRUCTURE = {
    "directories": [
        "src/",                     # 核心代码
        "scripts/",                 # 独立脚本
        "data/raw",                 # 原始数据
        "data/processed",           # 处理后的数据
        "data/outputs",             # 输出结果
        "tests/",                   # 单元测试
        "docs/",                    # 文档
        "config/",                  # 配置文件
        "notebooks/",               # Jupyter笔记
    ],
    "files": {
        ".gitignore": [
            "# PyCharm",
            ".idea/",
            "*.iml",
            "",
            "# Python",
            "__pycache__/",
            "*.py[cod]",
            "*.so",
            ".Python",
            "build/",
            "develop-eggs/",
            "dist/",
            "downloads/",
            "eggs/",
            ".eggs/",
            "lib/",
            "lib64/",
            "parts/",
            "sdist/",
            "var/",
            "wheels/",
            "*.egg-info/",
            ".installed.cfg",
            "*.egg",
            "",
            "# Virtual Environment",
            ".venv/",
            "venv/",
            "ENV/",
            "env.bak/",
            "",
            "# Data & Logs",
            "*.log",
            "*.sqlite",
            "*.csv~",
            "*.tmp",
            "",
            "# Jupyter",
            ".ipynb_checkpoints/",
            "*.ipynb",
        ],
        "README.md": [
            "# Project Title",
            "A brief description of your project.",
        ]
    }
}

def create_project(root_path="."):
    """ 创建项目结构 """
    root = Path(root_path)

    # 创建目录
    print("\n🛠️ 创建目录结构:")
    for dir_path in PROJECT_STRUCTURE["directories"]:
        full_path = root / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ {full_path}")

    # 创建文件
    print("\n📄 生成配置文件:")
    for file_name, content_lines in PROJECT_STRUCTURE["files"].items():
        file_path = root / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content_lines))
        print(f"✓ {file_path}")

    print("\n✅ 项目初始化完成！")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="初始化项目结构")
    parser.add_argument("-p", "--path", default=".", help="项目根目录路径（默认为当前目录）")
    args = parser.parse_args()

    create_project(args.path)