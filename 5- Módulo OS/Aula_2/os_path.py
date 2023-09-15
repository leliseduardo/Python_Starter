import os

os.getcwd()

os.path.join(os.getcwd(), 'pasta2')

os.path.basename(os.getcwd())

os.path.split(os.getcwd())[0]

os.path.dirname(os.getcwd())

curr_dir = os.getcwd()
lt = os.path.getatime(curr_dir)

from datetime import datetime

datetime.utcfromtimestamp(lt)

os.path.isfile(curr_dir)
os.path.isdir(curr_dir)