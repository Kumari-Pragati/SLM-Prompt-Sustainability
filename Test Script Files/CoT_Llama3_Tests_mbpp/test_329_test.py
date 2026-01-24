import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(neg_count([]), 0)

    def test_positive_list(self):
        self.assertEqual(neg_count([1, 2, 3]), 0)

    def test_mixed_list(self):
        self.assertEqual(neg_count([-1, 2, 0, 3]), 2)

    def test_all_negative_list(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_single_negative_number(self):
        self.assertEqual(neg_count([1, -2, 3]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(neg_count([-1, -1, 0, 1, 2]), 2)

    def test_list_with_negative_and_positive_duplicates(self):
        self.assertEqual(neg_count([-1, -1, 0, 0, 1, 1, 2, 2]), 4)
