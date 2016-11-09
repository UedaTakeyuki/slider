i2cdetect -y 1 | cut -c 4- | grep -o '[0-9,a-f][0-9,a-f]'
