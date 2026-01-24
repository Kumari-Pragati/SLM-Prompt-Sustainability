import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(angle_complex(1, 2), cmath.phase(complex(1, 2)))
        self.assertAlmostEqual(angle_complex(-1, 2), cmath.phase(complex(-1, 2)))
        self.assertAlmostEqual(angle_complex(1, -2), cmath.phase(complex(1, -2)))
        self.assertAlmostEqual(angle_complex(-1, -2), cmath.phase(complex(-1, -2)))

    def test_edge_cases(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), cmath.phase(complex(0, 1)))
        self.assertAlmostEqual(angle_complex(1, 0), cmath.phase(complex(1, 0)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 2)
        with self.assertRaises(TypeError):
            angle_complex(1, 'b')
