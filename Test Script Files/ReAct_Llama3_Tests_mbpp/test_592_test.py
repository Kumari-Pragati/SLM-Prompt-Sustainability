import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_sum_of_product_zero(self):
        self.assertEqual(sum_Of_product(0), 0)

    def test_sum_of_product_one(self):
        self.assertEqual(sum_Of_product(1), 1)

    def test_sum_of_product_positive(self):
        self.assertEqual(sum_Of_product(2), 2)

    def test_sum_of_product_negative(self):
        with self.assertRaises(TypeError):
            sum_Ofproduct(-1)

    def test_sum_of_product_non_integer(self):
        with self.assertRaises(TypeError):
            sum_Ofproduct(2.5)

    def test_sum_of_product_large(self):
        self.assertEqual(sum_Ofproduct(100), 495)
