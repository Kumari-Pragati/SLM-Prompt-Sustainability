import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)

    def test_single_element(self):
        self.assertEqual(max_product_tuple([1]), 0)
        self.assertEqual(max_product_tuple([-1]), 0)
        self.assertEqual(max_product_tuple([0]), 0)

    def test_positive_numbers(self):
        self.assertEqual(max_product_tuple([1, 2, 3, 4, 5]), 120)
        self.assertEqual(max_product_tuple([10, 20, 30, 40, 50]), 60000)

    def test_negative_numbers(self):
        self.assertEqual(max_product_tuple([-1, -2, -3, -4, -5]), 120)
        self.assertEqual(max_product_tuple([-10, -20, -30, -40, -50]), 60000)

    def test_mixed_numbers(self):
        self.assertEqual(max_product_tuple([1, -2, 3, -4, 5]), 60)
        self.assertEqual(max_product_tuple([-1, 2, -3, 4, -5]), 60)
        self.assertEqual(max_product_tuple([10, -20, 30, -40, 50]), 120000)
