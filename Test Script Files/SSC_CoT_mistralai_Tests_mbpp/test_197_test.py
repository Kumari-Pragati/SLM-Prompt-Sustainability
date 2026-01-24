import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertTupleEqual(find_exponentio((2, 3, 5), (7, 2, 4)), (125, 9, 625))
        self.assertTupleEqual(find_exponentio((-2, 3, -5), (7, 2, -4)), (-125, 9, 3125))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(find_exponentio((0, 3), (7, 2)), (0, 343))
        self.assertTupleEqual(find_exponentio((-2, 0), (7, 2)), (-1, 49))
        self.assertTupleEqual(find_exponentio((2, 0), (7, 2)), (1, 49))
        self.assertTupleEqual(find_exponentio((2, 3), (0, 2)), (2, 1))
        self.assertTupleEqual(find_exponentio((2, 3), (2, 0)), (2, 1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_exponentio, (2, 3, 5), 'not_a_number')
        self.assertRaises(TypeError, find_exponentio, 'not_a_number', (7, 2, 4))
