import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 3))

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3]), (-1, -3))

    def test_single_element(self):
        self.assertEqual(max_product([1]), None)

    def test_zero_element(self):
        self.assertEqual(max_product([]), None)

    def test_all_positive(self):
        self.assertEqual(max_product([10, 20, 30]), (10, 30))

    def test_all_negative(self):
        self.assertEqual(max_product([-10, -20, -30]), (-10, -30))

    def test_mixed_signs(self):
        self.assertEqual(max_product([1, -2, 3]), (1, 3))
