#输入用户姓名及性别，然后给出下列的提示

def chosex(name="",sex=""):
    mdict={
        '男':name+"先生，你好",
        '女':name+"女士，你好",
    }
    if sex == "男":
        print(mdict["男"])
    elif sex == "女":
        print(mdict["女"])
    elif sex!="男" or sex!="女":
        print("注意！输入性别时请输入，男/女")
