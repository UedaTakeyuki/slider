#!/bin/sh
#http://shokai.org/blog/archives/6893
#http://physicom.digick.jp/?p=5283
#http://moblog.absgexp.net/openjtalk/

TMP=/tmp/jsay.wav

#cd /usr/share/hts-voice/nitech-jp-atr503-m001
#cd /usr/share/hts-voice/mei_happy
echo start
echo "$1" | open_jtalk \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-m /home/pi/SCRIPT/slider/vendor/mei_normal.htsvoice \
-a 0.5 \
-ow $TMP && \
aplay --quiet $TMP
rm -f $TMP

