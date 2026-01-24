import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_small_input(self):
        self.assertEqual(sum_Of_product(1), 1)

    def test_medium_input(self):
        self.assertEqual(sum_Of_product(5), 16)

    def test_large_input(self):
        self.assertEqual(sum_Of_product(10), 252)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            sum_Of_product(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_Of_product(3.5)
