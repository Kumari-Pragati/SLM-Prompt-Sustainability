import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_positive_list(self):
        self.assertEqual(neg_count([1, 2, 3, 4, 5]), 0)

    def test_negative_list(self):
        self.assertEqual(neg_count([-1, -2, -3, -4, -5]), 5)

    def test_mixed_list(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(neg_count([1]), 0)

    def test_single_negative_element_list(self):
        self.assertEqual(neg_count([-1]), 1)
