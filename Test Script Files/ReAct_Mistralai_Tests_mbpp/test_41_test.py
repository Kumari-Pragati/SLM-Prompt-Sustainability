import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], filter_evennumbers([]))

    def test_single_even_number(self):
        self.assertListEqual([2], filter_evennumbers([2]))

    def test_single_odd_number(self):
        self.assertListEqual([], filter_evennumbers([3]))

    def test_mixed_numbers(self):
        self.assertListEqual([2, 4, 6], filter_evennumbers([1, 2, 3, 4, 5, 6]))

    def test_negative_numbers(self):
        self.assertListEqual([-2, -4, -6], filter_evennumbers([-2, -3, -4, -5, -6]))

    def test_large_numbers(self):
        self.assertListEqual([20, 22, 24, 26, 28], filter_evennumbers(range(10, 30, 2)))

    def test_list_with_zero(self):
        self.assertListEqual([0, 2, 4, 6], filter_evennumbers([0, 1, 2, 3, 4, 5, 6]))
