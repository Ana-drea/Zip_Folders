import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


def zipit(dir_list, zip_name):
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dir in dir_list:
        zipdir(dir, zipf)
    zipf.close()

folder = input("Type in the foler to zip:")

subfolders = os.listdir(folder)
absolute_paths = []
for subfolder in subfolders:
    absolute_paths.append(os.path.join(folder,subfolder))
zipit(absolute_paths, r"C:\Users\vivian\Downloads\test\test.zip")