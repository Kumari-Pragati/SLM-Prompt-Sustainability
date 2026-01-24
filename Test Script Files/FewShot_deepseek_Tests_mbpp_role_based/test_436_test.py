import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertEqual(neg_nos([1, -2, 3]), -2)

    def test_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_mixed_numbers(self):
        self.assertEqual(neg_nos([1, -2, 3, -4]), -2)

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-1]), -1)
