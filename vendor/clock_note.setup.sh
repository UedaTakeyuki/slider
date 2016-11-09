# © Atelier UEDA 2016 - 

# install requires
# http://think-bowl.com/raspberry-pi/installing-the-think-bowl-i2c-libraries-for-python/

mkdir quick2wire
cd quick2wire
here=`pwd`

git clone https://github.com/quick2wire/quick2wire-python-api.git
cd quick2wire-python-api
sudo python3 setup.py install
cd ..

cd ..
git clone https://bitbucket.org/thinkbowl/i2clibraries.git

#
# service file
#
cat << EOS1 > /etc/systemd/system/clock_note.service
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

