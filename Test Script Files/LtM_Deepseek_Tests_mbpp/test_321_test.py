import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_demlo("abc"), "12321")

    def test_empty_input(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character_input(self):
        self.assertEqual(find_demlo("a"), "1")

    def test_long_input(self):
        self.assertEqual(find_demlo("abcdefghijklmnopqrstuvwxyz"), "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100")

    def test_maximum_length_input(self):
        self.assertEqual(find_demlo("a"*321), "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100")
