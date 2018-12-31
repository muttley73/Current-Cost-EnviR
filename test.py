#!/usr/bin/python3

import re


text = '<msg>' \
       '<src>CC128-v1.19</src>' \
       '<uid>4410808100B8004-/\x0b4\xd8</uid>' \
       '<dsb>02863</dsb>' \
       '<time>17:17:52</time>' \
       '<tmpr>21.6</tmpr>' \
       '<sensor>0</sensor>' \
       '<id>01299</id>' \
       '<type>1</type>' \
       '<ch1>' \
       '<watts>01748</watts>' \
       '</ch1>' \
       '</msg>\r\n'

watts_ex = re.compile('<watts>([0-9]+)</watts>')
temp_ex = re.compile('<tmpr>([\ ]?[0-9\.]+)</tmpr>') # when temperature is less than 10, currentcost adds a space before the number
time_ex = re.compile('<time>([0-9\.\:]+)</time>')

watts = int(watts_ex.findall(text)[0]) # cast to and from int to strip leading zeros
temp = float(temp_ex.findall(text)[0]) # remove that extra space
time = str(time_ex.findall(text)[0])

print(watts)
print(temp)
print(time)