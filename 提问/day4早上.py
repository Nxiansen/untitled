print("异常是个对象，表示一个错误，用来管理程序执行期间发生的错误")
print("如果编写的异常不进行处理，程序将停止")
print("异常的代码块：try：【1】  except exception as e：【2】，异常的对象叫exception")
try:
    print(5/0)
except Exception as e:
    print(e)
print("手动抛出异常：raise Exception")
print("自定义异常：更灵活，扩展性强")
print("难点1：自建类抛出异常 2：异常的种类")
print("")
print("")