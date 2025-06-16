#!/bin/bash

sudo -v || { echo "incorrect password."; exit 1; }

mkdir -p ~/system_logs && touch ~/system_logs/syslog.txt
logfile="$HOME/system_logs/syslog.txt"
{
	echo "=== System Informations ==="
	fastfetch
	echo -e "\n=== Uptime ==="
	uptime

	echo -e "\n=== Disk Informations ==="
	df -h && free -h

	echo -e "\n=== Network Informations === "
	ip a

	echo -e "\n=== Open Ports ==="
	sudo ss -tuln

	echo -e "\n=== USERS ==="
	who


} >> "$logfile"

echo "Log file created !! : $logfile"
