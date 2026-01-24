import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertEqual(-5, neg_nos([-5]))

    def test_mixed_numbers(self):
        self.assertIsNone(neg_nos([1, -2, 3]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            neg_nos(['a', 'b', 'c'])

    def test_single_negative_number(self):
        self.assertEqual(-10, neg_nos([-10]))

    def test_single_positive_number(self):
        self.assertIsNone(neg_nos([10]))

    def test_multiple_negative_numbers(self):
        self.assertEqual(-20, neg_nos([-20, -10]))

    def test_multiple_positive_numbers(self):
        self.assertIsNone(neg_nos([10, 20]))
