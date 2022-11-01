import os

path = os.getcwd()
directories = []
files = []
for (dir_path, dir_names, file_names) in os.walk(path):
    directories.extend(dir_names)
    files.extend(file_names)
    break

print("directories:", directories)
print("files:", files)
