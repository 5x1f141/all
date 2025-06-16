#!/bin/bash

read -p "wanna send ping first? (y/n) : " x

if [[ "$x" == "y" ]]; then

	read -p "IP Adress : " y

	ping  $y

	nmap -sV $y

else

	echo ""

fi

read -p "Enter a IP : " ip

nmap -sV $ip
