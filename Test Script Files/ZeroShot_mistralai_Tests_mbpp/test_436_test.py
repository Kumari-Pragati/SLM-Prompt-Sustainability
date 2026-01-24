import unittest
from mbpp_436_code import neg_nos

class TestNegativeNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_positive_list(self):
        self.assertIsNone(neg_nos([1, 2, 3, 4]))

    def test_negative_list(self):
        self.assertEqual(neg_nos([-1, 0, 2, -3]), -1)

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-5, 0, 3]), -5)

    def test_single_positive_number(self):
        self.assertIsNone(neg_nos([5, 0, -3]))
