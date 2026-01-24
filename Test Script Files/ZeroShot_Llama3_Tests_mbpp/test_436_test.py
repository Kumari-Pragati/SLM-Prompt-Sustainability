import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(neg_nos([1, 2, 3]), None)

    def test_negative_numbers(self):
        self.assertEqual(neg_nos([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(neg_nos([1, -2, 3, -4]), -2)

    def test_empty_list(self):
        self.assertEqual(neg_nos([]), None)

    def test_single_positive_number(self):
        self.assertEqual(neg_nos([5]), None)

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-5]), -5)

    def test_single_zero(self):
        self.assertEqual(neg_nos([0]), None)
