filename = input("Input the Filename: ")
f = filename.split(".")
if f[1]=="py":
    print ("The extension of the file is : 'python'" )
elif f[1]=="c":
    print ("The extension of the file is : 'C'" )
elif f[1]=="cpp":
    print ("The extension of the file is : 'C++'" )
else:
    print("Invalid Extension")
