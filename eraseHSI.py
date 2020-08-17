import os
os.chdir('HSI')
path = os.getcwd()




myFiles=os.listdir(path)
for f in myFiles:
        with open(f, "r+", encoding='utf-8') as files:
            if os.stat(f).st_size != 0:
                files.seek(0)
                files.truncate()  # 清空文件
