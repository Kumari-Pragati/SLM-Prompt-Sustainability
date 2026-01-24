import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_simple_even_numbers(self):
        self.assertListEqual(filter_evennumbers([2, 4, 6]), [2, 4, 6])

    def test_simple_odd_numbers(self):
        self.assertListEqual(filter_evennumbers([1, 3, 5]), [])

    def test_empty_list(self):
        self.assertListEqual(filter_evennumbers([]), [])

    def test_single_number(self):
        self.assertListEqual(filter_evennumbers([0]), [0])

    def test_min_max_values(self):
        self.assertListEqual(filter_evennumbers(range(0, 100)), list(range(0, 100, 2)))

    def test_negative_numbers(self):
        self.assertListEqual(filter_evennumbers([-2, -4, -6]), [-2, -4])

    def test_mixed_numbers(self):
        self.assertListEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4])
