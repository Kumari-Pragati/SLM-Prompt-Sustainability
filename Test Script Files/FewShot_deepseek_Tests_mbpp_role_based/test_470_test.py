import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5))

    def test_edge_condition(self):
        self.assertEqual(add_pairwise(()), ())

    def test_boundary_condition(self):
        self.assertEqual(add_pairwise((1,)), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_pairwise(123)
        with self.assertRaises(TypeError):
            add_pairwise((1, 2, 'a'))
