import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_find_char(self):
        self.assertEqual(find_char("Hello world"), ['Hel', 'lo', 'wor', 'ld'])
        self.assertEqual(find_char("Python is a great language"), ['Pyt', 'hon', 'is', 'a', 'gra', 'et', 'lan', 'gua', 'ge'])
        self.assertEqual(find_char("1234567890"), [])
        self.assertEqual(find_char("abcdefghijklmnopqrstuvwxyz"), ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'])
        self.assertEqual(find_char(""), [])
