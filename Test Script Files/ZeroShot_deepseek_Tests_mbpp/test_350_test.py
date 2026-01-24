import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_minimum_Length(self):
        self.assertEqual(minimum_Length('aabcb'), 2)
        self.assertEqual(minimum_Length('aabbcc'), 0)
        self.assertEqual(minimum_Length('abcabc'), 0)
        self.assertEqual(minimum_Length('aabbccdd'), 4)
        self.assertEqual(minimum_Length(''), 0)
        self.assertEqual(minimum_Length('a'), 0)
        self.assertEqual(minimum_Length('ab'), 0)
        self.assertEqual(minimum_Length('aaaabbbb'), 0)
        self.assertEqual(minimum_Length('abcdefghijklmnopqrstuvwxyz'), 25)
