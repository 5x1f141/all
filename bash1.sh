#!/bin/bash
RAPOR="rapor-$(date +%Y-%m-%d_%H-%M-%S).txt"
echo "### System Information Log ###" > $RAPOR
echo "Date : $(date)" >> $RAPOR
echo "User : $USER" >> $RAPOR
echo "" >> $RAPOR


echo ">> UPTIME : " >> $RAPOR
uptime >> $RAPOR
echo "" >> $RAPOR

echo ">> Ram Usage : " >> $RAPOR
free -h >> $RAPOR
echo "" >>$RAPOR
echo ">>Disk Usage : " >> $RAPOR
df -h >> $RAPOR
echo "" >> $RAPOR
echo ">>IP Adress : " >> $RAPOR
ip a | grep inet >> $RAPOR

echo "[✓] Rapor oluşturuldu: $RAPOR"
