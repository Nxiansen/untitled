class MyException (ValueError):
    pass
try:
    print("before raise exception")

    #手动抛出异常
    raise MyException
    print("after raise exception")

    #捕获自定义异常
except MyException as me:
    print("catch MyException")

    #捕获自定义异常的父类
except ValueError as ve:
    print("catch ValueError")

    #捕获所有异常的父类
except Exception as e:
    print("exception")
    print(e)

    #如果没有异常发生则继续执行
else:
    print("exception")

finally:
    print("finally")