#
# https://github.com/guyc/py-gaugette
#
########################################

# wiring pi
# already installed

# wiringpi2-python
sudo apt-get install python-dev
sudo pip install setuptools
git clone https://github.com/Gadgetoid/WiringPi2-Python.git
cd WiringPi2-Python/
sudo python setup.py install
cd ..

# py-spidev
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
sudo python setup.py install
cd ..

# gdata-python-client
git clone https://github.com/google/gdata-python-client.git
cd gdata-python-client
sudo python setup.py install
cd ..

# adafruit-beaglebone-io-python
sudo apt-get install ntpdate
sudo apt-get install opkg
#/usr/bin/ntpdate -b -s -u pool.ntp.org
ntpdate -b -s -u pool.ntp.org
opkg update && opkg install python-pip python-setuptools python-smbus
sudo pip install smbus
sudo pip install Adafruit_BBIO

# py-gaugette
git clone https://github.com/guyc/py-gaugette.git
cd py-gaugette
sudo python setup.py install
cd ..

# omake: Adafruit_Python_SSD1306
sudo apt-get install python-imaging
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
cd ..
