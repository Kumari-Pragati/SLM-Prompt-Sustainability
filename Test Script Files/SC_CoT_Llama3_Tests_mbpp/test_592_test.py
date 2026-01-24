import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Ofproduct(4), 6)

    def test_special_or_corner_cases(self):
        self.assertEqual(sum_Of_product(-1), 1)
        self.assertEqual(sum_Of_product(0.5), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Of_product('a')
