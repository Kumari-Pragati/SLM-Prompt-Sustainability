import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_remove_char(self):
        self.assertEqual(remove_char("Hello, World!"), "HelloWorld")
        self.assertEqual(remove_char("Hello_World"), "HelloWorld")
        self.assertEqual(remove_char("Hello World"), "HelloWorld")
        self.assertEqual(remove_char("Hello"), "Hello")
        self.assertEqual(remove_char("1234567890"), "1234567890")
        self.assertEqual(remove_char("abc def"), "abcdef")
        self.assertEqual(remove_char("abc def gh"), "abcdefgh")
        self.assertEqual(remove_char("abc def gh ij"), "abcdefghij")
        self.assertEqual(remove_char("abc def gh ij kl"), "abcdefghijk")
        self.assertEqual(remove_char("abc def gh ij kl mn"), "abcdefghijkln")
        self.assertEqual(remove_char("abc def gh ij kl mn op"), "abcdefghijklnop")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr"), "abcdefghijklnopqr")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st"), "abcdefghijklnopqrst")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv"), "abcdefghijklnopqrstuv")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx"), "abcdefghijklnopqrstuvwxy")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz"), "abcdefghijklnopqrstuvwxyyz")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab"), "abcdefghijklnopqrstuvwxyyzab")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd"), "abcdefghijklnopqrstuvwxyyzabcd")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef"), "abcdefghijklnopqrstuvwxyyzabcdef")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh"), "abcdefghijklnopqrstuvwxyyzabcdefgh")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij"), "abcdefghijklnopqrstuvwxyyzabcdefghij")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl"), "abcdefghijklnopqrstuvwxyyzabcdefghijk")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn"), "abcdefghijklnopqrstuvwxyyzabcdefghijkln")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnop")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqr")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrst")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrstuv")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv wx"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrstuvwxy")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv wx yz"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrstuvwxyyz")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv wx yz ab"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrstuvwxyyzab")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv wx yz ab cd"), "abcdefghijklnopqrstuvwxyyzabcdefghijklnopqrstuvwxyyzabcd")
        self.assertEqual(remove_char("abc def gh ij kl mn op qr st uv wx yz ab cd ef gh ij kl mn op qr st uv wx yz ab cd ef"), "abcdefghijklnopqrst