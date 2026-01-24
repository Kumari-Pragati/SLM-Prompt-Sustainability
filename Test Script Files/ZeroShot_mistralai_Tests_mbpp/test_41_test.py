import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_evennumbers([]), [])

    def test_single_odd_number(self):
        self.assertListEqual(filter_evennumbers([1]), [])

    def test_single_even_number(self):
        self.assertListEqual(filter_evennumbers([2]), [2])

    def test_mixed_numbers(self):
        self.assertListEqual(filter_evennumbers([1, 2, 3, 4, 5, 6]), [2, 4])

    def test_all_even_numbers(self):
        self.assertListEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])
