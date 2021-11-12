#!/bin/bash
#Write a menu driven program for 1. Odd or Even Number 2. Find smallest number amongst three numbers
#Anushka Tadphale- 111903019
i="y"
while [ $i = "y" ]
do
echo "1.Odd or even"
echo "2.Smallest among three numbers"
echo "Enter your choice"
read ch
case $ch in
    1) echo "Enter number"
        read n1
        if (("$n1" % 2 =="0"));
        then
            echo "$n1 is an even number"
        else 
            echo "$n1 is an odd number"
        fi;;

    2) echo "Enter first number"
    read a
        echo "Enter second number"
        read b
        echo "Enter third number"
        read c
        
        if [ $b -lt $a ]
        then
            s=$b
        else
            s=$a
        fi
        if [ $c -lt $s ]
        then
            s=$c
        fi
        echo "Smallest of $a $b $c is $s" ;;
    
    *) echo "Invalid choice";;
esac
echo "Do u want to continue ?[y for yes/ n for no]"
read i
if [ $i != "y" ]
then
    exit
fi
done    