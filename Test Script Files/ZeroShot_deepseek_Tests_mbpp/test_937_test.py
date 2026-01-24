import unittest
from mbpp_937_code import Counter
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_max_char(self):
        self.assertEqual(max_char('aabbbcc'), 'b')
        self.assertEqual(max_char('abc'), 'a')
        self.assertEqual(max_char('aabbcc'), 'a')
        self.assertEqual(max_char(''), '')
        self.assertEqual(max_char('112233'), '1')
        self.assertEqual(max_char('aaaabbbcc'), 'a')
