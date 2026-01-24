import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 3)
        self.assertEqual(sum_Of_product(4), 6)
        self.assertEqual(sum_Of_product(5), 10)
        self.assertEqual(sum_Of_product(6), 15)
        self.assertEqual(sum_Of_product(7), 21)
        self.assertEqual(sum_Of_product(8), 28)
        self.assertEqual(sum_Of_product(9), 36)
        self.assertEqual(sum_Of_product(10), 45)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_product(0), 0)
        self.assertEqual(sum_Of_product(-1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Of_product('a')
        with self.assertRaises(TypeError):
            sum_Of_product(None)
