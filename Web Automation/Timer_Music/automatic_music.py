import time
import random
import pyttsx3
from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


playlist = ['unravel acoustics version english', 'peace sign jonathan young', 'homura english version ama lee', 'gurenge english version', 'overlord cattanoia english version jonathan', 'death note op 1 english jonathan young']

engine = pyttsx3.init()
engine.setProperty('rate', 130)

def autoplay():	
	
	browser.get('https://www.youtube.com')
	search_bar = browser.find_element_by_xpath('//*[@id="search"]')
	search_bar.send_keys(playlist[random.randint(0, len(playlist) - 1)] + Keys.RETURN)
	first_video = browser.find_element_by_xpath('//*[@id="img"]')
	first_video.click()

def popup():
	global browser
	engine.say(' Initiate Protocal Music ')
	engine.runAndWait()
	popup = messagebox.askquestion(' Play Music ', ' Initiate Protocal Music ? ')
	if popup == 'yes':
		browser = webdriver.Chrome(ChromeDriverManager().install())
		autoplay()
	else:
		engine.say(' Aborting Protocal Music ')
		engine.runAndWait()
		browser.close()
		

current_time = time.strftime('%I:%M:%S')

try:
	music_time = '06:22:00'  
except:
	music_time = '07:00:00'

while current_time != music_time:
	print('Time :'  + current_time )
	time.sleep(1)
	current_time = time.strftime('%I:%M:%S')

if current_time == music_time:
	popup()




