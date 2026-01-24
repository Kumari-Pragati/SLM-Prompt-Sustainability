import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertEqual(-5, neg_nos([-5, 2, 3]))

    def test_mixed_numbers(self):
        self.assertEqual(-2, neg_nos([-2, 1, 3]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_no_negative_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_single_negative_number(self):
        self.assertEqual(-1, neg_nos([-1]))

    def test_multiple_negative_numbers(self):
        self.assertEqual(-5, neg_nos([-5, -2, -1]))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            neg_nos(['a', 2, 3])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            neg_nos([1, 'b', 3])
