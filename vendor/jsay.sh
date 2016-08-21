#!/bin/sh
#http://shokai.org/blog/archives/6893
#echo こんばんは | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -ow ~/jtalk.wav
# http://physicom.digick.jp/?p=5283

TMP=/tmp/jsay.wav

#cd /usr/share/hts-voice/nitech-jp-atr503-m001
#cd /usr/share/hts-voice/mei_happy
echo start
echo "$1" | open_jtalk \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice \
-ow $TMP && \
aplay --quiet $TMP
rm -f $TMP

