import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):

    def test_typical_input(self):
        self.assertAlmostEqual(area_tetrahedron(5), 12.732050807568877)

    def test_edge_case_zero(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-5)

    def test_edge_case_zero_length(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(0)

    def test_edge_case_negative_length(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-5)

    def test_edge_case_zero_length(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(0)

    def test_edge_case_negative_length(self):
        with self.assertRaises(ValueError):
            area_tetrahedron(-5)

    def test_typical_input_float(self):
        self.assertAlmostEqual(area_tetrahedron(5.5), 24.432050807568877)

    def test_typical_input_string(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('five')

    def test_typical_input_list(self):
        with self.assertRaises(TypeError):
            area_tetrahedron([5])

    def test_typical_input_tuple(self):
        with self.assertRaises(TypeError):
            area_tetrahedron((5,))

    def test_typical_input_dict(self):
        with self.assertRaises(TypeError):
            area_tetrahedron({'side': 5})
