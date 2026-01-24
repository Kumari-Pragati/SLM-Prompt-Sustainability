import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Digits(0), 0)
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(2), 2)
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(100), 2)

    def test_negative_input(self):
        self.assertEqual(find_Digits(-1), 0)
        self.assertEqual(find_Digits(-10), 0)

    def test_edge_cases(self):
        self.assertEqual(find_Digits(10**10), 2)
        self.assertEqual(find_Digits(10**20), 2)

    def test_complex_inputs(self):
        self.assertEqual(find_Digits(1000), 4)
        self.assertEqual(find_Digits(10000), 4)
        self.assertEqual(find_Digits(100000), 5)
