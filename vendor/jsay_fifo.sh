#!/bin/sh
#http://shokai.org/blog/archives/6893
#echo こんばんは | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -ow ~/jtalk.wav
# http://physicom.digick.jp/?p=5283

#TMP=/tmp/jsay.wav
QUEUE=`mktemp -u`.fifo
mkfifo $QUEUE

#cd /usr/share/hts-voice/nitech-jp-atr503-m001
#cd /usr/share/hts-voice/mei_happy
echo start
echo "$1" | open_jtalk \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice \
-ow $QUEUE & \
aplay --quiet $QUEUE
rm -f $QUEUE

