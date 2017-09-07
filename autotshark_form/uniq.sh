#! /bin/bash
cat namelist.txt | uniq > temp.txt
rm namelist.txt
mv temp.txt namelist.txt 