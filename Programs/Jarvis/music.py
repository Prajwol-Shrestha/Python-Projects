from selenium import webdriver 

class music():
	browser = webdriver.Chrome()
	
	def play(self, name):
		self.name = name
		self.browser.get(url = "https://www.youtube.com/results?search_query=" + name)
		#search_button = self.browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
		#search_button.click()
		first_video  = self.browser.find_element_by_xpath('//*[@id="dismissable"]')
		first_video.click()




