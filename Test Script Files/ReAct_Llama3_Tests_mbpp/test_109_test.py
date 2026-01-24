import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)

    def test_edge_case_zero_length(self):
        self.assertEqual(odd_Equivalent('', 5), 0)

    def test_edge_case_zero_count(self):
        self.assertEqual(odd_Equivalent('000', 3), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_single_digit_zero(self):
        self.assertEqual(odd_Equivalent('0', 1), 0)

    def test_edge_case_single_digit_one(self):
        self.assertEqual(odd_Equivalent('1', 1), 1)

    def test_edge_case_multiple_digits(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)

    def test_edge_case_multiple_digits_zero(self):
        self.assertEqual(odd_Equivalent('000', 3), 0)

    def test_edge_case_multiple_digits_one(self):
        self.assertEqual(odd_Equivalent('101', 3), 2)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Equivalent(None, 5)
