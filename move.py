import os
import shutil

inputdir = r'C:\Users\l\Desktop\基于可见光图像的柑橘花果梢语义分割挑战赛公开数据-初赛\train\dataset'
outputdir = r'C:\Users\l\Desktop\基于可见光图像的柑橘花果梢语义分割挑战赛公开数据-初赛\train\labelpng'

# for dir in os.listdir(inputdir):
#     # print(os.sep)
#     # 设置旧文件名（就是路径+文件名）
#     oldname = inputdir + os.sep+dir+os.sep+'label.png'  # os.sep添加系统分隔符
#
#     # 设置新文件名
#     dir=dir.split('_')
#     # print(dir)
#     dir=dir[0:-1]
#     # print(dir)
#     dir_new='_'.join(dir)
#     # print(dir_new)
#     newname = outputdir + os.sep + dir_new + '.png'
#
#     shutil.copyfile(oldname, newname)  # 用os模块中的rename方法对文件改名
#     print(oldname, '======>', newname)
for dir in os.listdir(inputdir):
    # print(dir)
    # print(os.sep)
    # 设置旧文件名（就是路径+文件名）
    oldname = inputdir + os.sep+dir+os.sep+'label.png'  # os.sep添加系统分隔符

    # 设置新文件名
    dir=dir.split('_')
    # print(dir)
    dir=dir[0:-1]
    # print(dir)
    dir_new='_'.join(dir)
    # print(dir_new)
    newname = outputdir + os.sep + dir_new + '.png'
    print(newname)
    shutil.copyfile(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)