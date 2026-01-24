import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_all_positive_numbers(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([-1, 2, -3, 4, -5]), 3)

    def test_zero_in_list(self):
        self.assertEqual(neg_count([0]), 0)

    def test_large_list(self):
        self.assertEqual(neg_count(list(range(-1000, 1000))), 2000)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            neg_count("not a list")

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            neg_count(123)
