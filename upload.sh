#!/bin/bash

# 获取当前版本号并增加 0.0.1
current_version=$(grep 'version = ' pyproject.toml | cut -d'"' -f2)
IFS='.' read -r -a version_parts <<< "$current_version"
new_version="${version_parts[0]}.${version_parts[1]}.$(( ${version_parts[2]} + 1 ))"

# 更新 pyproject.toml 中的版本号
sed -i '' "s/version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml

echo "Version updated from $current_version to $new_version"

# 清理旧的构建文件
rm -rf dist/ build/ *.egg-info/

# 重新构建
uv run -m build

# 上传到 PyPI
uv run -m twine upload dist/*

# 提交版本更新到 git
git add pyproject.toml
git commit -m "bump version to $new_version"