from crypto import *
import unittest

class TestCrypto(unittest.TestCase):
    def test_morse(self, text):
        e= morse_encryption(text)
        d= morse_decryption(e)
        self.assertEqual(d, text.upper(), "Morse encryption decryption not working")
        print('Testing Morse: ')
        print('text: {}\nencrypted: {}\ndecrypted(in upper case): {}'.format(text, e, d))
        print()
    
    def bad_symbols(self, text):
        self.assertEqual(morse_encryption(text), 'You entered something beyond understanding!', "Morse encryption not working fine")
        print('Bad symbols: {} dont get encrypted'.format(text))
        print()
    #def test_
    def bad_morse(self, morse):
        self.assertEqual(morse_decryption(morse), 'Some wrong morse code!', "Morse decryption not working fine")
        print('Bad morse code: {} doesnt get decrypted'.format(morse))
        print()
        
    def test_caesar(self, text, s):
        e= caesar_encrypt(text, s)
        d= caesar_decrypt(e, s)
        self.assertEqual(d, text, 'Caesar cryptography not working')
        print('Testing Caesar cipher:')
        print('text: {} ; key: {}\nencrypted: {}\ndecrypted(in upper case): {}'.format(text, s, e, d))
        print()
    
    def bad_caesar(self, text, s):
        self.assertEqual(caesar_encrypt(text, s), 'Invalid characters', 'Caesar didnt detect invalid characters')
        print('text: {} ; key: {}\ncaesar encryption supports alphabetic and numeric characters only!'.format(text, s))
        print()
        
    def test_fernet(self):
        key= write_key()
        encrypt_fernet('demo.txt', key, 'encdemo.txt')
        decrypt_fernet('encdemo.txt', 'key.key', 'decdemo.txt')
        t= open('demo.txt', 'r').read()
        e= open('encdemo.txt', 'r').read()
        d= open('decdemo.txt', 'r').read()
        self.assertEqual(t, d, 'Fernet encryption not working')
        print('Testing Fernet file encryption:')
        print('Text: ', t)
        print('Encrypted: ', e)
        print('Decrypted: ', d)
        print()
        
    def test_nokey(self):
        print('Testing encryption without key: ')
        self.assertEqual(encrypt_fernet('demo.txt', None, 'enc.txt'), 'No key given', 'Encryption without key?')
        print('Result: ', encrypt_fernet('demo.txt', None, 'enc.txt'))
        print()
        
    def test_nofile(self):
        key= write_key()
        e= encrypt_fernet('nofile.txt', key, 'encdemo.txt')
        self.assertEqual(e, 'File not found' , 'Encryption without file?')
        print('Testing encryption on file which doesnot exist: ')
        print('Result: ', e)
        print()
        
    def test_dec(self):
        d= decrypt_fernet('decdemo.txt', 'abcd.key', 'enc12.txt')
        self.assertEqual(d, 'key file not found' , 'Decryption without key?')
        print('Testing encryption without key file: ')
        print('Result: ', d)
             

t= TestCrypto()
t.test_morse('anushka at COEP')
t.test_morse('Numeric symbols() 1.23?')
t.bad_symbols('Bad#*%>')
t.bad_morse('-...--- ..-. .. -.-.')

t.test_caesar('SE miniproject', 4)
t.test_caesar('Numeric also 456', 5)
t.bad_caesar('Bad symbols:?>', 8)

t.test_fernet()
t.test_nofile()
t.test_nokey()
t.test_dec()