from PIL import Image
import os
경로 = os.getcwd()
파일명들 = os.listdir(경로+'/images')

for i in 파일명들:
    img = Image.open('images/'+ i)
    img.thumbnail((500,2500))
    img.save('new_' + i)
    
# img = Image.open('images/photo1.jpg').convert('L')
# img.thumbnail((500,2500))
# img.save('new_photo1.jpg', quality=65)