# lib_seat
lib 备份
# Ubuntu 
- crontab -e 
  - 29 18 * * * /usr/bin/python3 /root/lib_seat/seat.py ?> /root/lib_seat/free.log
  - 50 7 * * * /usr/bin/python3 /root/lib_seat/Punch.py > /root/lib_seat/Punch.log
  - 47 8-22 * * * /usr/bin/python3 /root/lib_seat/guard.py ?> /root/lib_seat/guard.log
# shell
. seat_start.sh
