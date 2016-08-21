# git
sudo  apt-get install git-core

# addwpa
sudo apt-get install nkf
git clone https://github.com/UedaTakeyuki/addwpa.git

# pip
sudo apt-get install python-pip

# i2c
sudo apt-get install i2c-tools python-smbus

# WireingPi
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
cd ..

# fswebcam
sudo apt-get install fswebcam

# NGINX, php
sudo apt-get install nginx
sudo apt-get install php5-fpm
sudo sed -i 's|index index.html index.htm|index index.php index.html index.htm|g' /etc/nginx/sites-enabled/default
sudo sed -i 's|#location ~ \\\.php$ {|location ~ \\\.php$ {|' /etc/nginx/sites-e
sudo sed -i 's|#\tinclude snippets/fastcgi-php.conf;|\tinclude snippets/fastcgi-php.conf;|g' /etc/nginx/sites-enabled/default
sudo sed -i 's|#\tfastcgi_pass unix:/var/run/php5-fpm.sock;|\tfastcgi_pass unix:/var/run/php5-fpm.sock; }|g' /etc/nginx/sites-enabled/default
sudo apt-get install cryptsetup
sudo apt-get install wvdial eject usb-modeswitch

# NTFS
sudo apt-get install fuse ntfs-3g

# usb automount
#
#   http://raspberrypi.stackexchange.com/questions/41959/automount-various-usb-stick-file-systems-on-jessie-lite
sudo apt-get install usbmount
sudo sed -i 's|FILESYSTEMS="vfat ext2|FILESYSTEMS="vfat ntfs fuseblk ext2|g' /etc/usbmount/usbmount.conf
sudo sed -i 's|FS_MOUNTOPTIONS=""|FS_MOUNTOPTIONS="-fstype=ntfs-3g,nls=utf8,umask=007,gid=46 -fstype=fuseblk,nls=utf8,umask=007,gid=46 -fstype=vfat,gid=1000,uid=1000,umask=007"|g' /etc/usbmount/usbmount.conf

cat << EOS1 > /etc/udev/rules.d/usbmount.rules
KERNEL=="sd*", DRIVERS=="sbp2",         ACTION=="add",  PROGRAM="/bin/systemd-escape -p --template=usbmount@.service $env{DEVNAME}", ENV{SYSTEMD_WANTS}+="%c"
KERNEL=="sd*", SUBSYSTEMS=="usb",       ACTION=="add",  PROGRAM="/bin/systemd-escape -p --template=usbmount@.service $env{DEVNAME}", ENV{SYSTEMD_WANTS}+="%c"
KERNEL=="ub*", SUBSYSTEMS=="usb",       ACTION=="add",  PROGRAM="/bin/systemd-escape -p --template=usbmount@.service $env{DEVNAME}", ENV{SYSTEMD_WANTS}+="%c"
KERNEL=="sd*",                          ACTION=="remove",       RUN+="/usr/share/usbmount/usbmount remove"
KERNEL=="ub*",                          ACTION=="remove",       RUN+="/usr/share/usbmount/usbmount remove"
EOS1

cat << EOS2 > /etc/systemd/system/usbmount@.service
[Unit]
BindTo=%i.device
After=%i.device

[Service]
Type=oneshot
TimeoutStartSec=0
Environment=DEVNAME=%I
ExecStart=/usr/share/usbmount/usbmount add
RemainAfterExit=yes
EOS2

