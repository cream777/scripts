#!/bin/bash

#this is a simple bash script to ping ips on a network discretely

cat << "EOF"

This script is a simple ip sweeper that will print available hosts on a network.



EOF








read -p "please enter the first 3 sections of your target network address > " ip
read -p "enter start of range > " start_range
read -p "enter end of range > " end_range


echo -e "\nhosts available:\n"

for i in $(seq $start_range $end_range)
do

ping -c 1 -w 5 $ip.$i | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1 & 

done

wait
echo 

