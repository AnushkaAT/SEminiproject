#!/bin/bash
#Create a Bash script which will print a message based upon which day of the week it is (eg. 'Happy hump day' for Wednesday, 'TGIF' for Friday etc).
#Anushka Tadphale- 111903019
messages=('Hello Weekend'
          'Monday blues'
          'Tuesday Tweak Readers'
          'Happy hump day!'
          'Throwback Thursday'
          'TGIF'
          'Party night')

if [ -n "$1" ]
then 
    #day= "$1"
    echo "${messages[$1]}"
else
    echo "${messages[$(date +%w)]}"
fi