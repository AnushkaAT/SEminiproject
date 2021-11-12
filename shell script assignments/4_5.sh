#!/bin/bash
#Write a shell script to display files and folders from current directory.
#Anushka Tadphale- 111903019
echo "Current working directory: "
pwd
echo
echo "Files present: "

for file in *
do
    if [ -f "$file" ]
    then
    echo $file
    fi
done

echo
echo "Folders present: "
for dir in *
do 
    if [ -d "$dir" ]
    then
    echo $dir
    fi
done