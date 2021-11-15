import unittest
from crypto import morse_decryption, morse_encryption


class TestMorseA(unittest.TestCase):
    """This class only tests the morse_decryption function"""

    def test_word(self):
        self.assertEqual(morse_decryption('... --- ..-. - .-- .- .-. .'),
            'SOFTWARE')

    def test_basic_decoding(self):
        """Basic Morse decoding"""
        self.assertEqual(morse_decryption('.-'), 'A')
        self.assertEqual(morse_decryption('.'), 'E')
        self.assertEqual(morse_decryption('..'), 'I')

    def test_extra_spaces(self):
        self.assertEqual(morse_decryption(' . '), 'E')
        self.assertEqual(morse_decryption('   .   . '), ' E E')

    def test_complex(self):
        """Complex tests"""
        self.assertEqual(morse_decryption(
            '... --- ..-. - .-- .- .-. .  . -. --. .. -. . . .-. .. -. --.  -- .. -. .. .--. .-. --- .--- . -.-. - '),
            'SOFTWARE ENGINEERING MINIPROJECT'
        )
        
class TestMorseB(unittest.TestCase):
    """This class only tests the morse_encryption function"""

    def test_software(self):
        self.assertEqual(morse_encryption('CODING'),
            '-.-. --- -.. .. -. --. ')
    def test_basic_encoding(self):
        """Basic Morse decoding"""
        self.assertEqual(morse_encryption('X'), '-..- ')
        self.assertEqual(morse_encryption('Y'), '-.-- ')
        self.assertEqual(morse_encryption('Z'), '--.. ')

if __name__ == '__main__':
    unittest.main(verbosity=2)