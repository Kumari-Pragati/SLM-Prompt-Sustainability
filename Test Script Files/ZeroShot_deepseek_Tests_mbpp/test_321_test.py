import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_find_demlo_with_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_find_demlo_with_single_character(self):
        self.assertEqual(find_demlo("a"), "121")

    def test_find_demlo_with_multiple_characters(self):
        self.assertEqual(find_demlo("abc"), "123121")

    def test_find_demlo_with_long_string(self):
        self.assertEqual(find_demlo("abcdefghijklmnopqrstuvwxyz"), "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100")
