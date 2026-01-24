import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertEqual(-5, neg_nos([-5]))

    def test_mixed_numbers(self):
        self.assertEqual(-3, neg_nos([-3, 1, 2]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_all_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3, 4]))

    def test_all_negative_numbers(self):
        self.assertEqual(-5, neg_nos([-5, -3, -2]))

    def test_single_positive_number(self):
        self.assertIsNone(neg_nos([1]))

    def test_single_negative_number(self):
        self.assertEqual(-1, neg_nos([-1]))

    def test_single_zero(self):
        self.assertIsNone(neg_nos([0]))
