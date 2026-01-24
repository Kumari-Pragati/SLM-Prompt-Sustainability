import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 5)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_product(0), 0)
        self.assertEqual(sum_Of_product(1000), 332659130)

    def test_negative_input(self):
        self.assertRaises(ValueError, sum_Of_product, -1)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, sum_Of_product, 2.5)

    def test_zero_or_one_input(self):
        self.assertEqual(sum_Of_product(0), 0)
        self.assertEqual(sum_Of_product(1), 1)
