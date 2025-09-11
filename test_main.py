# 这个文件用于测试，不要修改其中的代码

import subprocess
import sys
import re

def run_program(input_value):
    """运行学生程序并捕获输出"""
    try:
        process = subprocess.run(
            [sys.executable, "main.py"],
            input=f"{input_value}\n",
            text=True,
            capture_output=True,
            timeout=5
        )
        return process.stdout, process.stderr
    except Exception as e:
        return "", str(e)

def test_palindrome():
    """主测试函数"""
    test_cases = [
        # 有效输入测试 (输入值, 预期输出)
        ("12321", "是回文数"),
        ("12345", "不是回文数"),
        ("11211", "是回文数"),
        ("54321", "不是回文数"),
        ("00000", "是回文数"),
        ("10101", "是回文数"),
        
        # 无效输入测试
        ("1234", "输入错误: 请输入5位数字"),
        ("123456", "输入错误: 请输入5位数字"),
        ("abcde", "输入错误: 请输入5位数字"),
        ("12a34", "输入错误: 请输入5位数字"),
        ("123.4", "输入错误: 请输入5位数字"),
        ("", "输入错误: 请输入5位数字")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for input_val, expected_output in test_cases:
        stdout, stderr = run_program(input_val)
        output = stdout.strip()
        
        # 检查是否有错误输出
        if stderr:
            print(f"❌ 程序执行错误: {stderr}")
            continue
        
        # 检查输出是否匹配
        if expected_output in output:
            print(f"✅ 测试通过: {input_val} -> {expected_output}")
            passed += 1
        else:
            print(f"❌ 测试失败: {input_val}")
            print(f"   预期: {expected_output} | 实际: {output}")
    
    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试通过!")
        exit(0)
    else:
        print("💥 存在未通过的测试")
        exit(1)

if __name__ == "__main__":
    test_palindrome()
