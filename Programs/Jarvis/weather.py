from selenium import webdriver
import pyttsx3
from selenium.webdriver.common.keys import Keys
import time

class weather():
	browser = webdriver.Chrome()
	

	def current_weather(self,place):
		self.place = place
		self.browser.get(url = 'https://www.accuweather.com/en/np/kathmandu/241809/weather-forecast/241809')
		T = self.browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[1]/div[1]/div/div/div[1]')
		readable_T = T.text
		
		A_value = self.browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]')
		readable_A_value = str(A_value) + 'AQI'
		A_text = self.browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[1]/div[2]/div/div[2]/h3/p[1]')
		readable_A = str(A_text)
		
		temp = 'Current Temperature is ' + readable_T
		air_quality = 'Air Quality is ' + readable_A_value + ' which is '+ readable_A

		current_weather = [temp, air_quality]

		engine = pyttsx3.init()
		#-------Speaking contents Inside the file		
		engine.say(current_weather[0] + current_weather[1])
		engine.runAndWait()
		time.sleep(10)
		self.browser.close()

bot = weather()
bot.current_weather()
