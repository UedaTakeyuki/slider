sudo sh -c 'cat << EOS1 > /etc/systemd/system/clock_note.service
[Unit]
Description=Sample Daemon
After=rc-local.service
[Service]
ExecStart=/usr/bin/python3 /home/pi/SCRIPT/slider/clock_note.py
Restart=always
Type=forking
PIDFile=/var/run/clock_note.pid
[Install]
WantedBy=multi-user.target
EOS1
'

sudo sh -c 'cat << EOS2 > /etc/systemd/system/clock_note2.service
[Unit]
Description=Sample Daemon
After=rc-local.service
[Service]
ExecStart=/usr/bin/python /home/pi/SCRIPT/slider/clock_note2.py
Restart=always
Type=forking
PIDFile=/var/run/clock_note.pid
[Install]
WantedBy=multi-user.target
EOS2
'

sudo systemctl daemon-reload
