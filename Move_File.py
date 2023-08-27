import os 
import shutil

from_dir = "C:/Users/Lenovo/Downloads"
to_dir = "C:/whitehat_jr/downloaded_images"
list_of_files = os.listdir(from_dir)

for f in list_of_files:
    name,extension = os.path.splitext(f)
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif','.pdf']:
        path1 = from_dir + '/' + f
        path2 = to_dir + '/' + "images_files"
        path3 = to_dir + '/' + "images_files" + '/' + f

        if os.path.exists(path2):
            shutil.move(path1 , path3)
        else : 
            os.makedirs(path2)
            shutil.move(path1 , path3)
            
