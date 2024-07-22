try:
    print(x)             #try block,exception block, else block finally block
except NameError:
    print("define x")
except:
    print("an error occured")





try:
    print(a)
except:
    print("an error occured")
else:
    print("no error")
finally:
    print("success")


x=-5
if x<0:
    raise Exception("-ve numbers r not allowed")