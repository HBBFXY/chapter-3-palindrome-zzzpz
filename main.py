def main():
    num = input().strip()
    
    if not num.isdigit() or len(num) != 5:
        print("输入错误: 请输入5位数字")
        return
        
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

if __name__ == "__main__":
    main()
