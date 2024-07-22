# # a=open("file1.txt","x")    #to crreate afile
# a=open("file1.txt","w")
# a.write("good morning have a nice day")
# a.close()


# a=open("file1.txt","r")
# print(a.read())
# a.close()



# b=open("file2.txt","x")


a=open("file1.txt","r")
x=a.read()
b=open("file2.txt","a")
b.write(x)
