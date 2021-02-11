# This UNZIPS all the nested zip files, just make sure they are in the same folder as this program, then> python unzipNested.py

import os

from zipfile import ZipFile


def unzip (path, total_count):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            if (not file_name.endswith('.zip')):
                total_count += 1
            else:
                currentdir = file_name[:-4]
                if not os.path.exists(currentdir):
                    os.makedirs(currentdir)
                with ZipFile(file_name) as zipObj:
                    zipObj.extractall(currentdir)
                os.remove(file_name)
                total_count = unzip(currentdir, total_count)
    return total_count

total_count = unzip ('.', 0)
print(total_count)