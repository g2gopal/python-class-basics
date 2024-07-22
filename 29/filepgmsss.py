#a=open("newfilepblm.txt","x")  #to craete a file



b=open("newfilepblm.txt","w")
b.write("hello there")
b.close()


b=open("newfilepblm.txt","r")
print(b.read())
b.close()




b=open("newfilepblm.txt","a")
b.write("\n have a great day")
b.close()



b=open("newfilepblm.txt","r")
print(b.read())
b.close()