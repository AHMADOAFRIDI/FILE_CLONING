import os, platform
os.system('git pull')
import requests
os.system("xdg-open https://www.facebook.com/profile.php?id=100009482583225")
bit = platform.architecture()[0]
if bit == '64bit':
    from FILE1 import menu
    menu()

