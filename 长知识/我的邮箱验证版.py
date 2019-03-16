if __name__ == '__main__':

    put=input("请输入邮箱：")
    if (put.find("@"))>0:
        if (put.find("."))>0:
            if put[0:7].__len__() >= 6:
                print("您输入的邮箱合法")
            else:
                print("姓名长度必须为6位或以上")
        else:
            print("邮箱格式中缺少 “.” 符号")
    else:
        print("邮箱格式中缺少 “@” 符号")