import unittest
from mbpp_588_code import List

from 588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(big_diff([]), 0)

    def test_single_element_list(self):
        self.assertEqual(big_diff([1]), 0)

    def test_two_elements_list(self):
        self.assertEqual(big_diff([1, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2]), 1)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(big_diff([-1, 1]), 2)

    def test_large_numbers(self):
        self.assertEqual(big_diff([1000000001, 1000000000]), 1)

    def test_list_with_duplicates(self):
        self.assertEqual(big_diff([1, 1, 2]), 1)

    def test_list_with_many_elements(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)
