import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 15)
        self.assertEqual(pair_OR_Sum([5, 5, 5, 5], 4), 0)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 31)

    def test_empty_list(self):
        self.assertEqual(pair_OR_Sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(pair_OR_Sum([1], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(pair_OR_Sum([-1, -2, -3], 3), 4)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            pair_OR_Sum([1, 2, 3], 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum('1, 2, 3', 3)
