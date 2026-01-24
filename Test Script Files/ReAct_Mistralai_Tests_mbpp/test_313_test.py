import unittest
from mbpp_313_code import pos_nos

class TestPositiveNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4]), [1, 2, 3, 4])

    def test_single_positive_number(self):
        self.assertEqual(pos_nos([5]), [5])

    def test_empty_list(self):
        self.assertEqual(pos_nos([]), [])

    def test_negative_numbers_in_list(self):
        self.assertEqual(pos_nos([-1, -2, -3]), [])

    def test_only_negative_number(self):
        self.assertEqual(pos_nos([-5]), [])

    def test_floats_in_list(self):
        self.assertEqual(pos_nos([0.0, 1.1, -2.2]), [1.1])

    def test_zero_in_list(self):
        self.assertEqual(pos_nos([0, 1, 2]), [1, 2])
