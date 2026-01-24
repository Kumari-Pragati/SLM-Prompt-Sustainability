import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(len_complex(3, 4), 5.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(len_complex(0, 0), 0.0)
        self.assertAlmostEqual(len_complex(1, 0), 1.0)
        self.assertAlmostEqual(len_complex(0, 1), 1.0)

    def test_edge_conditions(self):
        self.assertAlmostEqual(len_complex(-1, 0), 1.0)
        self.assertAlmostEqual(len_complex(0, -1), 1.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            len_complex('a', 1)
        with self.assertRaises(TypeError):
            len_complex(1, 'b')
        with self.assertRaises(TypeError):
            len_complex('a', 'b')
