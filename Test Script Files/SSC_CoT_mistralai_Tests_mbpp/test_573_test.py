import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(unique_product([1, 2, 3, 4]), 24)
        self.assertEqual(unique_product([5, 10, 15, 20]), 15000)

    def test_edge_cases(self):
        self.assertEqual(unique_product([0, 1, 2]), 2)
        self.assertEqual(unique_product([-1, 0, 1]), 1)
        self.assertEqual(unique_product([1, 1, 1]), 1)
        self.assertEqual(unique_product([1000000000, ]), 1000000000)

    def test_boundary_cases(self):
        self.assertEqual(unique_product([1]), 1)
        self.assertEqual(unique_product([1, ]), 1)
        self.assertEqual(unique_product([]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, unique_product, [1, 'a', 3])
        self.assertRaises(TypeError, unique_product, ['1', 2, 3])
