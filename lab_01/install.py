import os

os.system("sysctl -a hw > dev")
os.system("pyinstaller --onefile main.py")
