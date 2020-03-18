#!/bin/bash

while true

do
if [ $(date '+%M') == "00" ];then
        wget -O "$(date +'%Y%m%d_%H%M%S').csv" "http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.go$
        echo "download file at "$(date '+%Y%m%d_%H:%M:%S')
elif [ $(date '+%m%d') == "0321" ];then
        break
else
        echo $(date '+%Y%m%d_%H-%M-%S')
fi
sleep 60
done

