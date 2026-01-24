import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Digits(1234), 4)
        self.assertEqual(find_Digits(5678), 4)
        self.assertEqual(find_Digits(9101112), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(1), 1)
        self.assertEqual(find_Digits(10), 2)

    def test_invalid_or_exceptional_inputs(self):
        self.assertEqual(find_Digits(-1), 0)
