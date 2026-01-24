import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], filter_evennumbers([]))

    def test_single_number(self):
        self.assertListEqual([2], filter_evennumbers([2]))
        self.assertListEqual([], filter_evennumbers([1]))

    def test_positive_numbers(self):
        self.assertListEqual([2, 4, 6], filter_evennumbers([2, 4, 6, 8, 10]))

    def test_negative_numbers(self):
        self.assertListEqual([-2, -4, -6], filter_evennumbers([-2, -4, -6, -8, -10]))

    def test_mixed_numbers(self):
        self.assertListEqual([2, 4, 6, 8], filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8]))

    def test_zero(self):
        self.assertListEqual([0], filter_evennumbers([0]))
