#!/bin/bash
#Create a Bash script which will take two numbers as command line arguments. It will print to the screen the larger of the two numbers.
#Anushka Tadphale- 111903019
a="$1"
b="$2"
if [ $b -lt $a ]
then
    l=$a
else
    l=$b
fi
echo "Larger of $a $b is $l"