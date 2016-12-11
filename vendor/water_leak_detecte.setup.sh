sudo sh -c 'cat << EOS1 > /etc/systemd/system/water_leak_detecte.service
[Unit]
Description=Sample Daemon
After=rc-local.service
[Service]
ExecStart=/usr/bin/python /home/pi/SCRIPT/slider/water_leak_detecte.py
Restart=always
Type=forking
PIDFile=/var/run/water_leak_detecte.pid
[Install]
WantedBy=multi-user.target
EOS1
'

sudo systemctl daemon-reload
