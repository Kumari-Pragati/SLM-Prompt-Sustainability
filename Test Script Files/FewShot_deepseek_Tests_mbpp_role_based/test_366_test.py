import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 12)

    def test_edge_case(self):
        self.assertEqual(adjacent_num_product([1]), 0)

    def test_boundary_case(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            adjacent_num_product("1, 2, 3")

        with self.assertRaises(TypeError):
            adjacent_num_product(123)

        with self.assertRaises(TypeError):
            adjacent_num_product([1, "2", 3])

        with self.assertRaises(TypeError):
            adjacent_num_product([])
