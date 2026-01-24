import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), ((2 ** 4, 3 ** 5)))
        self.assertEqual(find_exponentio((10, 2), (3, 7)), ((10 ** 3, 2 ** 7)))

    def test_edge_conditions(self):
        self.assertEqual(find_exponentio((0, 0), (1, 1)), ((0, 1)))
        self.assertEqual(find_exponentio((1, 0), (1, 1)), ((1, 0)))
        self.assertEqual(find_exponentio((-1, 2), (3, 4)), ((-1 ** 3, 2 ** 4)))

    def test_boundary_conditions(self):
        self.assertEqual(find_exponentio((sys.maxsize,), (1,)), ((sys.maxsize ** 1,)))
        self.assertEqual(find_exponentio((1, sys.maxsize), (1,)), ((1, sys.maxsize ** 1)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_exponentio, (1, 'a'), (1, 1))
        self.assertRaises(TypeError, find_exponentio, (1, 1), ('a', 1))
