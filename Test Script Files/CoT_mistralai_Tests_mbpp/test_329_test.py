import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(neg_count([1, 3, 5, 7]), 0)

    def test_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([-1, 0, -2, 3, -4]), 3)

    def test_zero(self):
        self.assertEqual(neg_count([0]), 0)

    def test_floats(self):
        self.assertEqual(neg_count([-1.5, 0, 2.3]), 1)

    def test_list_of_lists(self):
        self.assertEqual(neg_count([[-1, 0, -2], [3, 4], [-5, -6, -7]]), 5)

    def test_invalid_input(self):
        self.assertRaises(TypeError, neg_count, "not a list")
