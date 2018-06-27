import urllib, re
import sys
from mechanize import Browser

url = "http://win2012-1/applidis/console/"

def connect_page():
	try:
		br = Browser()
		br.open(url)
		response = br.response
		print(response.read())
		return True
	except:
		print("Connection failed.")
		return False	

if connect_page() == True:
	print("[+] Connection succeed \n")
	# get dictionary in list
	login_list = []
	
	login_dico = raw_input("Entrez le chemin du dictionnaire de login: ")
	with open(login_dico) as login_fd:
		for login in login_fd.readlines():
			login_list.append(login.rstrip('\n'))
	login_fd.close()

	# get pwd in list
	pwd_list = []

	pwd_dico = raw_input("Entrez le chemin du dictionnaire de mdp: ")
	with open(pwd_dico) as pwd_fd:
		for pwd in pwd_fd.readlines():
			pwd_list.append(pwd.rstrip('\n'))
	pwd_fd.close()

	for login in login_list:
		for pwd in pwd_list:
			print(login, pwd)
