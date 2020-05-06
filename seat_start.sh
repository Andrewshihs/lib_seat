sudo chmod 777 seat.py
sudo chmod 777 guard.py
sudo chmod 777 Punch.py
sudo chmod 777 new.json
crontab -l > conf && echo "29 18 * * * /usr/bin/python3 /root/lib_seat/seat.py ?> /root/lib_seat/free.log" >> conf && crontab conf && rm -f conf
crontab -l > conf && echo "50 7 * * * /usr/bin/python3 /root/lib_seat/Punch.py > /root/lib_seat/Punch.log" >> conf && crontab conf && rm -f conf
crontab -l > conf && echo "47 8-22 * * * /usr/bin/python3 /root/lib_seat/guard.py ?> /root/lib_seat/guard.log" >> conf && crontab conf && rm -f conf
echo "finsh"
