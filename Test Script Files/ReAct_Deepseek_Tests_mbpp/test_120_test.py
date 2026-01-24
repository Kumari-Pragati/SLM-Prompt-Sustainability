import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        list1 = [(1, 2), (3, 4), (-1, -2)]
        self.assertEqual(max_product_tuple(list1), 6)

    def test_negative_numbers(self):
        list1 = [(-1, -2), (-3, -4), (-5, -6)]
        self.assertEqual(max_product_tuple(list1), 10)

    def test_positive_numbers(self):
        list1 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(max_product_tuple(list1), 12)

    def test_zero_numbers(self):
        list1 = [(0, 2), (3, 0), (5, 0)]
        self.assertEqual(max_product_tuple(list1), 0)

    def test_single_tuple(self):
        list1 = [(1, 2)]
        self.assertEqual(max_product_tuple(list1), 2)

    def test_empty_list(self):
        list1 = []
        self.assertIsNone(max_product_tuple(list1))

    def test_large_numbers(self):
        list1 = [(1000000000, 2000000000), (-3000000000, -4000000000)]
        self.assertEqual(max_product_tuple(list1), 20000000000000000000)
