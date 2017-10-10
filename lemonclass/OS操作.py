'''import os
dir1=os.getcwd()
dir2=os.path.join(dir1,"6666")
os.mkdir(dir2)
print(type(os.listdir(dir2)))

os.mkdir("D:\\666666")'''

from PIL import ImageGrab
im=ImageGrab.grab()
im.save("aaa.jpg",'jpeg')



