import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_simple_positive(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), 90)
        self.assertAlmostEqual(angle_complex(1, 1), 45)

    def test_simple_negative(self):
        self.assertAlmostEqual(angle_complex(-1, 0), 180)
        self.assertAlmostEqual(angle_complex(0, -1), 270)
        self.assertAlmostEqual(angle_complex(-1, -1), 315)

    def test_edge_cases(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)
        self.assertAlmostEqual(angle_complex(1e-6, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1e-6), 90)

    def test_complex_inputs(self):
        self.assertAlmostEqual(angle_complex(1, 1j), 45)
        self.assertAlmostEqual(angle_complex(1j, 1), 135)
        self.assertAlmostEqual(angle_complex(-1, -1j), 225)
        self.assertAlmostEqual(angle_complex(-1j, -1), 360)
