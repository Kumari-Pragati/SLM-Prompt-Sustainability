import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(neg_count([1, 2, 3, -1, 0, -2]), 2)

    def test_edge_case(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)
        self.assertEqual(neg_count([0, 0, 0]), 0)
        self.assertEqual(neg_count([1, 2, 3]), 0)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_single_element(self):
        self.assertEqual(neg_count([1]), 0)
        self.assertEqual(neg_count([-1]), 1)
        self.assertEqual(neg_count([0]), 1)

    def test_multiple_negative_numbers(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_multiple_positive_numbers(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(neg_count([-1, 2, -3, 4, -5]), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            neg_count('abc')
