from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3

class meaning:
	browser = webdriver.Chrome()

	def word(self,word):
		self.word = word
		self.browser.get(url = 'https://www.dictionary.com/')
		search_bar = self.browser.find_element_by_xpath('//*[@id="searchbar_input"]')
		query = search_bar.send_keys(word + Keys.RETURN)
		result = self.browser.find_element_by_xpath('//*[@id="base-pw"]/main/section/section/div[1]/section[2]/div/div')
		
		readable_text = result.text
		engine = pyttsx3.init()
		engine.say(readable_text)
		engine.runAndWait()
		
		self.browser.close()

bot = meaning()
bot.word('python')