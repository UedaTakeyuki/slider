# http://elinux.org/RPi_HardwareHistory
cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'
