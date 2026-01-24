import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_sum_Of_product_positive_integers(self):
        self.assertEqual(sum_Of_product(5), 155)
        self.assertEqual(sum_Of_product(10), 1820)
        self.assertEqual(sum_Of_product(15), 5005)

    def test_sum_Of_product_zero(self):
        self.assertEqual(sum_Of_product(0), 1)

    def test_sum_Of_product_negative_integers(self):
        self.assertEqual(sum_Of_product(-5), 1)
        self.assertEqual(sum_Of_product(-10), 1)
        self.assertEqual(sum_Of_product(-15), 1)

    def test_sum_Of_product_non_integers(self):
        with self.assertRaises(TypeError):
            sum_Of_product(5.5)
        with self.assertRaises(TypeError):
            sum_Of_product('5')
