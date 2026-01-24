import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 6)

    def test_single_element(self):
        self.assertEqual(big_sum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2, -3]), -1)

    def test_max_min_same(self):
        self.assertEqual(big_sum([5, 5, 5]), 10)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            big_sum([])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            big_sum([1, 2, '3'])

    def test_large_numbers(self):
        self.assertEqual(big_sum([10**10, 10**10]), 20000000000)
