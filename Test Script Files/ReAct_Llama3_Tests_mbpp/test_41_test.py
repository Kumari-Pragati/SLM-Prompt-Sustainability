import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvennumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_single_even(self):
        self.assertEqual(filter_evennumbers([2]), [2])

    def test_single_odd(self):
        self.assertEqual(filter_evennumbers([3]), [])

    def test_multiple_even(self):
        self.assertEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_multiple_odd(self):
        self.assertEqual(filter_evennumbers([1, 3, 5, 7]), [])

    def test_mixed(self):
        self.assertEqual(filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])

    def test_negative_numbers(self):
        self.assertEqual(filter_evennumbers([-2, -4, -6, -8]), [-2, -4, -6, -8])

    def test_zero(self):
        self.assertEqual(filter_evennumbers([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 2, 4, 6, 8])
