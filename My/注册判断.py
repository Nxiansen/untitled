if __name__ == '__main__':
    uname=input("请输入用户名:")
    if len(uname)>6 and len(uname)<16 and uname.isalnum():
        pwd=input("请输入密码:")
        if len(pwd)>6 and len(pwd)<16 and pwd.isalnum():
            print("用户{unamekey}的密码为{pwdkey}".format(unamekey=uname,pwdkey=pwd))
        else:
            print("密码6-16位，不允许出现*#!")
    else:
        print("用户名允许数字字母6-16位，不允许出现*#!")