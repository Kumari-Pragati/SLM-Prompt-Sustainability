import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_typical_case(self):
        self.assertTupleEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1.2246063538223773e-16+1.2246063538223773e-16j)))

    def test_boundary_case(self):
        self.assertTupleEqual(polar_rect(0, 0), ((0, 0), (0+0j)))

    def test_edge_case(self):
        self.assertTupleEqual(polar_rect(1, 0), ((1, 0), (1+0j)))
        self.assertTupleEqual(polar_rect(0, 1), ((1.5707963267948966, 1.5707963267948966), 1.2246063538223773e-16+1.2246063538223773e-16j))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 1)
        with self.assertRaises(TypeError):
            polar_rect(1, 'b')
        with self.assertRaises(TypeError):
            polar_rect('a', 'b')
