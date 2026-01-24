import unittest
from mbpp_124_code import angle_complex
import cmath

class TestAngleComplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), cmath.phase(complex(1, 1)))

    def test_boundary_conditions(self):
        self.assertAlmostEqual(angle_complex(0, 0), cmath.phase(complex(0, 0)))
        self.assertAlmostEqual(angle_complex(1, 0), cmath.phase(complex(1, 0)))
        self.assertAlmostEqual(angle_complex(0, 1), cmath.phase(complex(0, 1)))

    def test_edge_conditions(self):
        self.assertAlmostEqual(angle_complex(-1, 0), cmath.phase(complex(-1, 0)))
        self.assertAlmostEqual(angle_complex(0, -1), cmath.phase(complex(0, -1)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 1)
        with self.assertRaises(TypeError):
            angle_complex(1, 'b')
        with self.assertRaises(TypeError):
            angle_complex('a', 'b')
