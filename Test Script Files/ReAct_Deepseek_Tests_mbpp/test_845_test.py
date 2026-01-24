import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(1234), 4)
        self.assertEqual(find_Digits(999999), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(-1), 0)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(find_Digits('abc'), 0)
        self.assertEqual(find_Digits(None), 0)
