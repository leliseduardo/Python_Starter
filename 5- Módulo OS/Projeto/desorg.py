import os

def rename_files(file_origin, file_destination):
  for file in os.listdir(file_origin):
    os.rename(file_origin + "\\" + file, file_destination + "\\" + file)


for file in os.listdir(os.getcwd()):
  if(os.path.isdir(file) and file != "__pycache__"):
    file_origin = os.getcwd() + '\\' + file
    file_destination = os.getcwd()
    rename_files(file_origin, file_destination)
    os.rmdir(file)