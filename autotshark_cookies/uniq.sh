#! /bin/bash
cat namelist.txt | sort | uniq > temp.txt
rm namelist.txt
mv temp.txt namelist.txt 