import os

def no_repeat(dir):
  for file in os.listdir(os.getcwd()):
    if(file == dir):
      return False
  return True

for file in os.listdir(os.getcwd()):
  dir_name = file.split('.')[-1]
  if(no_repeat(dir_name) and dir_name != "py"):
    os.mkdir(dir_name)
  if(dir_name != "py" and os.path.isfile(file)):
    os.rename(os.getcwd() + "\\" + file, os.getcwd() + "\\" + dir_name + "\\" + file)
  




