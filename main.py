import os
import shutil

def organize_files(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            ext = filename.split('.')[-1]
            ext_dir = os.path.join(path, ext)
            os.makedirs(ext_dir, exist_ok=True)
            shutil.move(os.path.join(path, filename), os.path.join(ext_dir, filename))

