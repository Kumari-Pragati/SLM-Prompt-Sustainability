import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_simple_even_list(self):
        self.assertListEqual(remove_odd([0, 2, 4, 6]), [0, 2, 4])

    def test_simple_odd_list(self):
        self.assertListEqual(remove_odd([1, 3, 5]), [])

    def test_empty_list(self):
        self.assertListEqual(remove_odd([]), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_odd([1]), [])

    def test_min_max_values(self):
        self.assertListEqual(remove_odd(range(0, 100)), [1, 3, 5, 7, 9])

    def test_negative_numbers(self):
        self.assertListEqual(remove_odd([-1, -3, -5]), [])

    def test_mixed_list(self):
        self.assertListEqual(remove_odd([0, 1, 2, 3, 4, 5]), [0, 2, 4])
