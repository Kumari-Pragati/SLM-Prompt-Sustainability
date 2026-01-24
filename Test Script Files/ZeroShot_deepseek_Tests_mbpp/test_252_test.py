import unittest
from mbpp_252_code import polar
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert(1+1j), polar(1+1j))
        self.assertEqual(convert(0), polar(0))
        self.assertEqual(convert(-1-1j), polar(-1-1j))
        self.assertEqual(convert(1), polar(1))
        self.assertEqual(convert(-1), polar(-1))
