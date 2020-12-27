#你想获取文件系统中某个目录下的所有文件列表。
import os
fileList = os.listdir('folder')
import fnmatch import fnmatch
pyfile = [filePy for filePy in os.listdir('folder') if fnmatch(filePy,'*.py')]
import glob
import os
import os.path
pyfiles = glob.glob('*.py')
name_size_date = [(name,os.path.getsize(name),os.path.getmtime(name)) for name in pyfiles]
detail = [(name,os.stat(name)) for name in pyfiles]

