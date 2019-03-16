if __name__ == '__main__':
    def user():
        em = input("请输入正确的邮箱地址:")
        if len(em) >= 6 and "@" in em and "." in em:
            print("输入正确")
        else:
            print("输入格式有误")