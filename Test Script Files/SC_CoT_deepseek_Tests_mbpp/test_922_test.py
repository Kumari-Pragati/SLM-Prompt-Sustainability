import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_edge_case(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_boundary_case(self):
        self.assertEqual(max_product([0, 1, 2, 3]), (0, 3))

    def test_special_case(self):
        self.assertEqual(max_product([-1, -2, 3, 4]), (3, 4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_product("1, 2, 3, 4")

        with self.assertRaises(TypeError):
            max_product(123)

        with self.assertRaises(TypeError):
            max_product(None)

        with self.assertRaises(TypeError):
            max_product([1, 2, 3, "4"])

        with self.assertRaises(TypeError):
            max_product([1, 2, None, 4])
