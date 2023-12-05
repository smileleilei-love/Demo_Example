"""
程晓磊小伙伴学习python
2023/11/29 16:24
# @Author : cxl
# @File : Pyspark.py
"""

from pyspark import SparkContext


# 计算字符串s的hashcode
def hashcode(s):
    # 初始化hashcode为0
    h = 0
    # 遍历字符串s中的每一个字符
    for c in s:
        # 计算hashcode
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    # 返回hashcode
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000


# 计算文件哈希值
def select_file(file_path):
    # 打开文件
    with open(file_path, "r") as f:
        # 返回文件内容的哈希值
        return hashcode(f.read())


file_path = './smid'
result = select_file(file_path)

if __name__ == "__main__":
    print(result % 2000)
