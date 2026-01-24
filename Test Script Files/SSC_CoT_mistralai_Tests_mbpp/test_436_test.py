import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(neg_nos([1, 2, -3, 4]), -3)

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-5]), -5)

    def test_all_negative_numbers(self):
        self.assertEqual(neg_nos([-5, -4, -3, -2, -1]), -5)

    def test_positive_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3, 4]))

    def test_zero(self):
        self.assertIsNone(neg_nos([0]))

    def test_floats(self):
        self.assertEqual(neg_nos([1.5, -2.3, 3.7]), -2.3)

    def test_mixed_types(self):
        self.assertRaises(TypeError, neg_nos, [1, 2, -3, 4, 'five'])
