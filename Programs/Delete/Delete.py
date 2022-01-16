import os
import shutil

response = input("Do You want to remove a file or a folder: ")

file_response = ["file", "File"]
if response in file_response:
	directory = input("Enter the directory in which the file resides: ")
	file = input("Enter the name of the file: ")
	try:
		print("\n")
		print("----------PLEASE WAIT-----------")
		print("\n")
		os.remove(directory + '/'+ file)
		print("Deleting " + file +" ...")
		print("\n")
		print("File " + file + " deleted sucessfully")
		print("\n")
	except FileNotFoundError:
		print("Error: File Not Found!!")
else:
	pass

folder_response = ["folder", "Folder"]
if response in folder_response:
	folder = input ("Enter the name of the folder: ")
	print("\n")
	print(f"Deleting {folder} folder also deletes it's inside files")
	print("\n")
	decision = input(f"Are You sure you want to delete {folder} folder, Press y/n: ")
	if decision == "y":
		try:
			print("\n")
			print("----------PLEASE WAIT-----------")
			print("\n")
			shutil.rmtree(folder)
			print("Deleting " + folder +" ...")
			print("\n")
			print("File " + folder + " deleted sucessfully")
			print("\n")
		except:
			print("Error: File Not Found!!")
else:
	pass				
