import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(add_pairwise((1, 2, 3)), (3, 5))

    def test_edge_conditions(self):
        self.assertEqual(add_pairwise(()), ())
        self.assertEqual(add_pairwise((1,)), ())

    def test_complex_cases(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 7))
        self.assertEqual(add_pairwise((0, 0, 0)), (0, 0))
        self.assertEqual(add_pairwise((-1, -2, -3)), (-1, -1))
