import os, platform
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from FILE1 import menu
    menu()

