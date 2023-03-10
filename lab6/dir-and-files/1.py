import os
path=r'C:\Users\ASUS\Desktop\study\PP2\lab6\dir-and-files'
print("directories:", [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("files:", [name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("directories and files :", [name for name in os.listdir(path)])