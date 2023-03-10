import os
path=r'C:\Users\ASUS\Desktop\study\PP2\lab6\dir-and-files'
print("exists" if os.path.exists(path) else "not")
print("file name: " , os.path.basename(path))
print("directory portion: ", os.path.dirname(path))