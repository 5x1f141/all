#!/bin/bash


sudo -v || { echo "Sudo başarısız oldu."; exit 1; }

mkdir -p ~/system_logs
logfile="~/system_logs/syslog_$(date +%F_%T).txt"


{
    echo "=== Sistem Bilgisi ==="
    fastfetch || neofetch

    echo -e "\n=== Uptime ==="
    uptime

    echo -e "\n=== Disk Durumu ==="
    df -h

    echo -e "\n=== Bellek Durumu ==="
    free -h

    echo -e "\n=== Ağ Bilgisi ==="
    ip a

    echo -e "\n=== Açık Portlar ==="
    sudo ss -tuln

    echo -e "\n=== Kullanıcılar ==="
    who
} > "$logfile"

echo "Log dosyası kaydedildi: $logfile"
