import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(sum_digits_twoparts(1234), 10)
        self.assertEqual(sum_digits_twoparts(9876), 30)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(sum_digits_twoparts(0), 0)
        self.assertEqual(sum_digits_twoparts(10000), 10)
        self.assertEqual(sum_digits_twoparts(999999999), 90)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(sum_digits_twoparts(1000000000), 10)
        self.assertEqual(sum_digits_twoparts(1999999999), 20)
        self.assertEqual(sum_digits_twoparts(9999999999), 90)
