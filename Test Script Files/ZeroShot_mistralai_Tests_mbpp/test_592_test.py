import unittest
from592_code import sum_Of_product, binomial_Coeff

class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product_with_positive_integer(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 3)
        self.assertEqual(sum_Of_product(3), 15)
        self.assertEqual(sum_Of_product(4), 105)
        self.assertEqual(sum_Of_product(5), 645)

    def test_sum_of_product_with_zero(self):
        self.assertEqual(sum_Of_product(0), 1)

    def test_sum_of_product_with_negative_integer(self):
        self.assertRaises(ValueError, sum_Of_product, -1)

    def test_binomial_coeff_with_positive_integer(self):
        self.assertEqual(binomial_Coeff(2, 0), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(3, 0), 1)
        self.assertEqual(binomial_Coeff(3, 1), 3)
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(4, 0), 1)
        self.assertEqual(binomial_Coeff(4, 1), 4)
        self.assertEqual(binomial_Coeff(4, 2), 6)
        self.assertEqual(binomial_Coeff(4, 3), 4)

    def test_binomial_coeff_with_zero(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)

    def test_binomial_coeff_with_negative_integer(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 0)
        self.assertRaises(ValueError, binomial_Coeff, 0, -1)
