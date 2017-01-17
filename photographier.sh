#!/bin/bash

function usage() {
cat <<_EOT_
Usage:
  $0 filepath videodevice width_hight

Description:
  Take a photo from [videodevice] with [width_hight], save to [filepath]

Options:

_EOT_
exit 1
}

if [ $# -ne 3 ]; then
  usage
fi

filepath=$1
videodevice=$2
width_hight=$3

if [ $videodevice = "dummy" ]; then
# command_str = 'fswebcam '+filepath+' -d TEST -r 320x240'
  fswebcam $filepath -d TEST -r $width_hight
else
# command_str = 'fswebcam '+filepath+' -d /dev/'+videodevice+' -D 1 -S 20 -r 320x240'
  fswebcam $filepath -d /dev/$videodevice -D 1 -S 20 -r $width_hight
fi
exit 0