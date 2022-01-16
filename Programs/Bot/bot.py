import time
import os
import speedtest
from PyDictionary import PyDictionary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


greetings = ['hello','hi','namaste', 'Hello','Hi','Namaste']
WHQ = ["How are you?","how are you?",  "how are you", "what's up?",  "what's up"]
who = ["Who are you?", 'who are you?', "who are you", 'what are you?']
music = ['music', 'Music', 'Play music', 'play music']
shutdown = ['shutdown', 'sleep']
response = ['Ok', 'Affirmative']
speedcheck = ['check connection', 'check speed', 'speed', 'internet speed','speed test']
shutdown_timer = ['shutdown timer', 'Shutdown timer','timer']

print("\n")
print("\n")
print(' <-------- Interactive Bot -----> ')
while True:
	print("\n")
	print("\n")
	user = input("YOU : ")

	if user in greetings:
		print("\n")
		print(" Greetings User! ")
		print('\n')
		time.sleep(2)
		print(" What can I do for you today? ")

	elif user in WHQ:
		print('\n')
		print("I am a bot so that question does not applies to me.")
		print('\n')
		time.sleep(1)
		print('So, How are you?')
		print('\n')
		AWHQ = input('	YOU : ' )
		print('\n')

		p = ['fine','Fine', 'good', 'I am ok', 'i am ok']
		n = ['Not fine', 'not fine','not good', 'I am not ok', 'i am ok']
		
		if AWHQ in p:
			print(" 	That's Good ")
		elif AWHQ in n:
			print(' 	Hang in There ')
		else:
			print('		Ok')

	elif user in who:
		print('\n')
		print(' I am a personalised bot created by Prajwol Shrestha.')
		print('\n')
		print('######## This program is a bunch of if statements. ########')
		print('         This program is for specific prupose only ########')
		print('######## based on user preference.                 ########')		

	elif user in music:
		try: 
			print('\n')
			print(' Affirmative! Playing Music From YouTube.. ')

			browser = webdriver.Chrome(ChromeDriverManager().install())
			browser.get("https://www.youtube.com/watch?v=83RUhxsfLWs&list=RD83RUhxsfLWs&start_radio=1")
			pause_button = browser.find_element_by_xpath('//*[@id="movie_player"]/div[34]/div[2]/div[1]/button')
			pause_button.click()
		except ConnectionError:
			print("Connection Error!")
		except:
			print("Some Error Occured!")

	elif user in shutdown:
		print('\n')
		print(' Computer Will Now Shutdown in 5 minutes! ')
		print('\n')
		print(" Sayonara User ")
		os.system("shutdown /s /t 1")
	
	elif user == "meaning":
		while True:
			print('\n')
			print(' 	Enter back to terminate the loop ')
			print('\n')
			word = input("	 Enter the word: ")
			dictionary=PyDictionary(word)

			if word == "back":
				break

			print('\n')
			print('		Showing the Results for ' +  word)
			print('\n')
			print('		<----- Meaning -----> ')
			print('\n')
			print(dictionary.meaning(word))
			print('\n')
			print('		<----- Synonyms -----> ')
			print('\n')
			print(dictionary.synonym(word))
			print('\n')
			print(' 	<----- Antonyms -----> ')
			print('\n')
			print(dictionary.antonym(word))
			
	elif user in speedcheck:
		try:
			test = speedtest.Speedtest()
			print('\n')
			print('Getting Server List...')

			test.get_servers()

			print('\n')
			print('Getting the Best Server...')

			best = test.get_best_server()

			print('\n')
			print(f"Host Name: {best['host']} \nCountry: {best['country']}")

			print('\n')
			print('Checking Download Speed...')
			download = test.download()
			print('\n')
			print('Checking Upload Speed...')
			upload = test.upload()
			print('\n')
			print('Checking Ping...')
			ping = test.results.ping

			print('\n')
			print(f'Download Speed 	: {download/ 1024 / 1024:.2f} Mbit/s')
			print('\n')
			print(f'Upload Speed 	: {upload/ 1024 / 1024:.2f} Mbit/s')
			print('\n')
			print(f'Ping	: {ping:.2f} ms')
		except:
			print('\n')
			print('An Error Occured! \nPlease Try Again.')

	elif user in shutdown_timer:
		print('\n')
		timer = input('Enter timer(minutes): ')
		print('\n')
		print(f'Timer Set to {timer} Minutes')
		time.sleep(int(timer) * 60)
		os.system("shutdown /s /t 1")
		
	else:
		print("\n")
		print(" Sorry!, Could Not Get That ")	