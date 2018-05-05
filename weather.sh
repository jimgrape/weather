#!/usr/bin/env bash
#查天气的工具
if [ "$*"x == x ];then
    cityname="南京"
else
    cityname=$*
fi
for i in `echo ${cityname}`; do
echo --------------${i}------------------
w3m "http://cn.bing.com/search?q=${i}天气" > tmp
beginline=`cat -n  tmp | grep "实时天气"|awk '{print $1}'`
echo -n "(实时)"
cat tmp | awk "NR>${beginline}" | head -n 24 | sed 's/\[th\]//g' | tr '\n' ' ' |sed 's/\s\s*/ /g'\
    | sed 's/温度/\n温度/' | sed 's/今天/\n(今天)/' |sed 's/明天/\n(明天)/' |sed 's/后天/\n(后天)/'
echo
rm tmp
done
