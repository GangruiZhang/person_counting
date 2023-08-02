from sklearn.model_selection import train_test_split
import os

imagedir = r'E:\labelpng'
outdir = r'E:\imageseg'
testdir=r'C:\Users\l\Desktop\基于可见光图像的柑橘花果梢语义分割挑战赛公开数据-初赛\test\image'
images = []
test=[]
for file in os.listdir(imagedir):
    filename = file.split('.')[0]
    images.append(filename)
for file in os.listdir(testdir):
    filename = file.split('.')[0]
    test.append(filename)
# train, test = train_test_split(images, train_size=0.7, random_state=0)
# val, test = train_test_split(test, train_size=0.2 / 0.3, random_state=0)
# print(images)
# print(outdir)
with open(outdir + "\\train.txt", 'w') as f:
    f.write('\n'.join(images))

with open(outdir + "\\val.txt", 'w') as f:
    f.write('\n'.join(images))

with open(outdir + "\\test.txt", 'w') as f:
    f.write('\n'.join(test))

with open(outdir + "\\trainval.txt", 'w') as f:
    f.write('\n'.join(images))