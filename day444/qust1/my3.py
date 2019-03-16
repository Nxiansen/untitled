#注意一个用户信息，包含EMAIL号，判断信息是否合法，
# 如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）（30分）
def Email():
    put=input("请输入邮箱：")
    if int(put.find("@"))>0:
        if put[0:7].__len__()>=6:
            if put.endswith(".com") or put.endswith(".cn"):
                print("邮箱正确")
            else:
                print("请以“com” 或“cn”为后缀")
        else:
            print("请输入6位或以上的邮箱名字")
    else:
        print("您输入的邮箱缺少“@”符号")