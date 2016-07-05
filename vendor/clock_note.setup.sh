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

