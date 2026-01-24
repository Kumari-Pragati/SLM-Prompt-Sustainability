import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Digits(10), 2)
        self.assertEqual(find_Digits(121), 3)
        self.assertEqual(find_Digits(111), 3)

    def test_edge_conditions(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(-1), 0)

    def test_complex_cases(self):
        self.assertEqual(find_Digits(100), 2)
        self.assertEqual(find_Digits(999), 3)
        self.assertEqual(find_Digits(1000), 3)
