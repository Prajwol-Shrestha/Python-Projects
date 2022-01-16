email = input("Enter your email address: ").strip()

try:
 email_username = email[:email.index('@')]

 email_domain = email[email.index('@')+1:]

 print("Your username is " + email_username)

 print("Your domain name is " + email_domain)

except:
	print("Not a valid email address")	