#########################
#
# FOR SLIDER
#
########################
#python3
sudo apt-get install python3 python3-setuptools python3-pip

#getrpimodel written by UEDA
sudo pip install getrpimodel

#pytoml
sudo pip install pytoml

#paho
sudo pip install paho-mqtt

#serial
sudo pip install pyserial

#subprosess32
sudo pip install subprocess32

#requests
sudo pip install requests

#fswebcam
sudo apt-get install fswebcam

#
# WiringPi-Python
#
sudo apt-get install python-dev python-setuptools swig
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git
cd WiringPi-Python
# need following C library for swig, even if wiringpi is already installed. 
cd WiringPi
sudo ./build
cd ..
swig2.0 -python wiringpi.i
sudo python setup.py install
sudo python3 setup.py install
