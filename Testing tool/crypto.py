#!/usr/bin/env python3
from cryptography.fernet import Fernet
''' 
This script runs different algorithms in cryptography(encryption and decryption)
1. Morse code
2. Caeser cipher
3. Transposition cipher
4. Encryping files using Fernet
'''

#Morse code encryption decryption
#translates english letters to morse code
morsecode = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

dec= dict([(v, k) for k, v in morsecode.items()])
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#encrypt from english to morse code
def morse_encryption(message):
    message= message.upper()
    cipher= ''
    for letter in message:
        if letter== ' ':
            cipher+= ' '
        elif letter in morsecode.keys():
            cipher+= morsecode[letter] + ' '
        else:
            cipher= 'You entered something beyond understanding!'
            return cipher
    return cipher

#decrypt morse code to english
def morse_decryption(cipher):
    message= ''
    words= cipher.split('  ')
    for w in words:
        letters= w.split(' ')
        for l in letters:
            if(l in dec.keys()):
                message+= dec[l]
            elif(l== ''):
                pass
            else:
                message= 'Some wrong morse code!'
                return message
        if(len(words)>2 and w!= words[len(words)-1]):
            message+= ' '
    return message

def caesar_encrypt(text, s, choice= 'e'):
    cipher= ""
    for i in text:
        #upper case letters
        if(i.isupper()):
            cipher+= chr((ord(i) + s-65)% 26 + 65)
        
        #lower case letters
        elif(i.islower()):
            cipher+= chr((ord(i) + s-97)% 26 + 97)
            
        elif(i.isnumeric()):
            k= s % 10
            if(choice== 'd'):
                k= (26-s)%10
                k= 10-k
            cipher+= chr((ord(i) + k - 48)% 10 + 48)
            
        elif(i== ' '):
            cipher+= ' '
        
        else:
            return 'Invalid characters'
            
    return cipher

def caesar_decrypt(cipher, key):
    msg= ""
    msg= caesar_encrypt(cipher, 26-key, 'd')
    return msg

def write_key():
    #generated key and stores into file
    key= Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key
    
def load_key(keyfile):
    try:
        with open(keyfile, 'rb') as kf:
            key= kf.read()
            return key
    except:
        return -1

def encrypt_fernet(filename, key, dfile):
    if(key== None):
        return 'No key given'
    f= Fernet(key)
    try:
        with open(filename, 'rb') as file:
            file_data= file.read()
        edata= f.encrypt(file_data)
        #print(edata)
        with open(dfile, 'wb') as file:
            file.write(edata)
    except:
        return 'File not found'

def decrypt_fernet(filename, keyfile, efile):
    key= load_key(keyfile)
    if(key== -1):
        #print('key file not found')
        return 'key file not found'
    f= Fernet(key)
    try:
        with open(filename, 'rb') as file:
            edata= file.read()
        decdata= f.decrypt(edata)
        #print(decdata)
        with open(efile, 'wb') as file:
            file.write(decdata)
    except:
        #print('filenot found')
        return 'File not found'

def menu():
    m= "\n--------Menu--------\n"
    m+= "1. Morse encryption \n2. Morse decryption \n"
    m+= "4. Caesar-cipher encryption \n5. Caesar-cipher decryption\n"
    m+= "6. Transposition cipher encryption \n7. Transposition cipher decryption\n"
    m+= "8. Fernet file encryption \n9. Fernet file decryption\n"
    m+= "10. Exit"
    return m
 
def menucaller(choice):
    pass

'''text= 'AnUsHkA 123'
ciph= caesar_encrypt(text, 4)
t= caesar_decrypt(ciph, 4)
print(text, ciph, t)'''

'''e=morse_encryption('anushka')
print(e)
d= morse_decryption(e)
print(d)'''
