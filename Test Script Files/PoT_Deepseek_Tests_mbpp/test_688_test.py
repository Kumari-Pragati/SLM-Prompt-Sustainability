import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_typical_cases(self):
        self.assertAlmostEqual(len_complex(3, 4), 5.0)
        self.assertAlmostEqual(len_complex(-1, 0), 1.0)
        self.assertAlmostEqual(len_complex(0, -2), 2.0)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(len_complex(0, 0), 0.0)
        self.assertAlmostEqual(len_complex(1, 1), cmath.sqrt(2).real)
        self.assertAlmostEqual(len_complex(-1, -1), cmath.sqrt(2).real)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            len_complex('a', 4)
        with self.assertRaises(TypeError):
            len_complex(3, 'b')
        with self.assertRaises(TypeError):
            len_complex('a', 'b')
