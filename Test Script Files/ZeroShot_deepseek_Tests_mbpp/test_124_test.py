import unittest
from mbpp_124_code import phase
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_angle_complex(self):
        self.assertAlmostEqual(angle_complex(1, 1), phase(complex(1, 1)))
        self.assertAlmostEqual(angle_complex(0, 0), phase(complex(0, 0)))
        self.assertAlmostEqual(angle_complex(1, 0), phase(complex(1, 0)))
        self.assertAlmostEqual(angle_complex(0, 1), phase(complex(0, 1)))
        self.assertAlmostEqual(angle_complex(-1, -1), phase(complex(-1, -1)))
        self.assertAlmostEqual(angle_complex(-1, 0), phase(complex(-1, 0)))
        self.assertAlmostEqual(angle_complex(0, -1), phase(complex(0, -1)))
