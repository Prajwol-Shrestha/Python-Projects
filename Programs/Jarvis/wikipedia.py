from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class wiki():
	browser = webdriver.Chrome()

	def wikipedia(self, term):
		self.term = term
		self.browser.get(url = 'https://www.wikipedia.org/')
		search_bar = self.browser.find_element_by_xpath('//*[@id="searchInput"]')
		query = search_bar.send_keys(term + Keys.RETURN)
		content = self.browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li')
		time.sleep(10)
		self.browser.close()

bot = wiki()
bot.wikipedia('python programming')
