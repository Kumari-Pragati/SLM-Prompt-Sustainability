import unittest
from mbpp_742_code import area_tetrahedron

class TestAreaTetrahedron(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_tetrahedron(5), 37.699051093817271)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            area_tetrahedron('five')

    def test_edge_case_non_numeric2(self):
        with self.assertRaises(TypeError):
            area_tetrahedron(None)

    def test_edge_case_non_numeric3(self):
        with self.assertRaises(TypeError):
            area_tetrahedron([5])

    def test_edge_case_non_numeric4(self):
        with self.assertRaises(TypeError):
            area_tetrahedron({'five'})
