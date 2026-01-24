import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_case(self):
        self.assertTupleEqual(find_exponentio((2, 3, 5), (7, 2, 4)), (125, 9, 625))

    def test_edge_case_zero(self):
        self.assertTupleEqual(find_exponentio((0, 3), (7, 2)), (0, 49))

    def test_edge_case_negative(self):
        self.assertTupleEqual(find_exponentio((-2, 3), (7, 2)), (8, 49))

    def test_edge_case_float(self):
        self.assertAlmostEqual(find_exponentio((2.5, 3), (7, 2)), 45.875)

    def test_edge_case_mixed_types(self):
        self.assertRaises(TypeError, find_exponentio, (2, "3"), (7, 2))
