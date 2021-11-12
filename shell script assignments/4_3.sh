#!/bin/bash
#Create a Bash script which will accept a file as a command line argument and analyse it in certain ways. 
#eg. you could check if the file is executable or writable. You should print a certain message if true and another if false.
#Anushka Tadphale- 111903019

echo "Enter filename or path: "
read filename

if [ -x $filename ]
then    
    echo "$filename has executing permission"
else
    echo "$filename does not have executing permission"
fi 

if [ -w $filename ]
then    
    echo "$filename has writing permission"
else
    echo "$filename does not have writing permission"
fi

if [ -r $filename ]
then 
    echo "$filename has reading permission"
else
    echo "$filename does not have reading  permission"
fi