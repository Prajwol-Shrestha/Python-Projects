import speech_recognition as sr
from pyttsx3 import speak
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mics = sr.Microphone.list_microphone_names()
print(mics)

#Speech to text
r = sr.Recognizer()

with sr.Microphone(device_index = 1) as source:
	r.adjust_for_ambient_noise(source, 5)
	speak('Say Something!')

	audio = r.record(source, duration = 2)

	try:
		recognize = r.recognize_google(audio, language = 'en-NP')
		speak('You Said: ' + recognize)
		
		#============ Play music ===========

		if 'play' or 'music' in recognize:
			class music():
				browser = webdriver.Chrome()

				speak('Which music?')
				name = r.record(source, duration = 2)
				name_recognize = r.recognize_google(name, language = 'en-NP')
	
				def play(self):
					#self.name_recognize = name_recognize
					self.browser.get(url = "https://www.youtube.com/results?search_query=" + name_recognize)
					#search_button = self.browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
					#search_button.click()
					first_video  = self.browser.find_element_by_xpath('//*[@id="dismissable"]')
					first_video.click()

			bot = music()
			bot.play()

		#============ Weather ===========	
		if 'weather' in recognize:
			class weather():
				browser = webdriver.Chrome()
				speak('Which Place?')
				place = r.record(source, duration = 2)
				place_recognize = r.recognize_google(place, language = 'en-NP')

				def current_weather(self):
					self.browser.get(url = 'https://www.accuweather.com/en/np/kathmandu/241809/weather-forecast/241809')
					T = self.browser.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[1]/div[1]/div/div/div[1]')
					readable_T = T.text
					#################################################
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

		#============ Wkikipedia ==========
		if 'wikipedia' in recognize:
			class wiki():
				browser = webdriver.Chrome()

				speak('Query?')
				term = r.record(source, duration = 2)
				term_recognize = r.recognize_google(term, language = 'en-NP')

				def wikipedia(self):
					self.browser.get(url = 'https://www.wikipedia.org/')
					search_bar = self.browser.find_element_by_xpath('//*[@id="searchInput"]')
					query = search_bar.send_keys(term_recognize + Keys.RETURN)
					content = self.browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li')
					time.sleep(10)
					self.browser.close()

			bot = wiki()
			bot.wikipedia()

		#=========== Meaning ===========	
		if 'meaning' in recognize:
			class meaning:
				browser = webdriver.Chrome()
			
				speak('Query?')
				word = r.record(source, duration = 2)
				word_recognize = r.recognize_google(word, language = 'en-NP')
			
				def word(self):
					self.browser.get(url = 'https://www.dictionary.com/')
					search_bar = self.browser.find_element_by_xpath('//*[@id="searchbar_input"]')
					query = search_bar.send_keys(word_recognize + Keys.RETURN)
					result = self.browser.find_element_by_xpath('//*[@id="base-pw"]/main/section/section/div[1]/section[2]/div/div')
					
					readable_text = result.text
					engine = pyttsx3.init()
					engine.say(readable_text)
					engine.runAndWait()
					
					self.browser.close()

			bot = meaning()
			bot.word()	

	except sr.UnknownValueError:
		speak("Could Not get that")
	except sr.RequestError as e:
		speak("Could not request results from google; {0}".format(e))