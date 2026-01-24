import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_zero(self):
        self.assertEqual(neg_count([0]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            neg_count("not a list")
