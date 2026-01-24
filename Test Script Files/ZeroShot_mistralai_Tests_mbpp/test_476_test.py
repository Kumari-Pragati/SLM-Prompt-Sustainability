import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(big_sum([]), None)

    def test_single_element_list(self):
        self.assertEqual(big_sum([1]), 1)

    def test_two_elements_list(self):
        self.assertEqual(big_sum([1, 2]), 3)

    def test_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2]), 1)

    def test_large_numbers(self):
        self.assertEqual(big_sum([1000000001, 1000000002]), 2000000003)
