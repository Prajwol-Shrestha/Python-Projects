from bs4 import BeautifulSoup as bs
import requests
import time


def toonily():
	with open('toonily.html', 'w') as file:
		url = 'https://www.toonily.net'
		html = requests.get(url).text

		soup = bs(html, 'lxml')

		mangas = soup.find_all('div', class_='page-item-detail manga')

		print("\n")
		print("Gathering Required Info From toonily.net ..")
		print('\n')
		time.sleep(3)
		print("Cross Checking Updated Mangas with manga-list.txt")
		print('\n')
		time.sleep(3)
		
		for manga in mangas:
			title = manga.find('h3', class_= 'h5').a.text
			chapter = manga.find('div', class_ = 'list-chapter').span.a.text
			link = manga.find('span', class_ = 'chapter font-meta').a['href']

			with open('manga-list.txt', 'r') as f:
				lines = f.read()
				li = list(lines.split('\n'))

			if title in li:
				file.write(f'<h2 style="text-align:center;"> {title} </h2>')
				file.write(f'<h4 style="text-align:center;"> {chapter}</h4>')
				file.write(f'<a href="{link}" target =_blank style="padding-left:25em;"> Read Now..</a> ')

		print("Compiling Updated Mangas into html file..")
		print('\n')
		time.sleep(3)		
		print('Process Finished. \nFile Saved in Same Directory.')


def manhuaplus():
	with open('manhuaplus.html', 'w') as file:
		url = 'https://manhuaplus.com/'
		html = requests.get(url).text

		soup = bs(html, 'lxml')

		mangas = soup.find_all('div', class_='col-6 col-md-3 badge-pos-1')

		print("\n")
		print("Gathering Required Info From manhuaplus.com ..")
		print('\n')
		time.sleep(3)
		print("Cross Checking Updated Mangas with manga-list.txt")
		print('\n')
		time.sleep(3)
		
		for manga in mangas:
			title = manga.find('h3', class_= 'h5').a.text
			chapter = manga.find('div', class_ = 'list-chapter').span.a.text
			link = manga.find('span', class_ = 'chapter font-meta').a['href']

			with open('manga-list.txt', 'r') as f:
				lines = f.read()
				li = list(lines.split('\n'))

			if title in li:
				file.write(f'<h2 style="text-align:center;"> {title} </h2>')
				file.write(f'<h4 style="text-align:center;"> {chapter}</h4>')
				file.write(f'<a href="{link}" target =_blank style="padding-left:25em;"> Read Now..</a> ')

		print("Compiling Updated Mangas into html file..")
		print('\n')
		time.sleep(3)		
		print('Process Finished. \nFile Saved in Same Directory.')



if __name__ == "__main__":
	while True:
		toonily()
		manhuaplus()
		refresh_after = 60 # Minutes
		print('\n')
		print(f'Refreshing After {refresh_after} Minutes')
		time.sleep(refresh_after*60)