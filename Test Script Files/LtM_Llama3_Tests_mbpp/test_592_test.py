import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_product(-1), 1)
        self.assertEqual(sum_Of_product(3), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Of_product('a')
        with self.assertRaises(TypeError):
            sum_Of_product(None)

    def test_complex_inputs(self):
        self.assertEqual(sum_Of_product(5), 10)
        self.assertEqual(sum_Of_product(10), 45)
