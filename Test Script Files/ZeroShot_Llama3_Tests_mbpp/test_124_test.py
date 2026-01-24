import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_angle_complex(self):
        self.assertAlmostEqual(angle_complex(1,1), 0.7853981633974483)
        self.assertAlmostEqual(angle_complex(1,2), 0.4636476090008057)
        self.assertAlmostEqual(angle_complex(2,1), 1.1071487179410402)
        self.assertAlmostEqual(angle_complex(1,-1), 4.712389770196246)
        self.assertAlmostEqual(angle_complex(-1,1), 2.3561944901923448)
        self.assertAlmostEqual(angle_complex(-1,-1), 5.497787143782138)

    def test_angle_complex_zero(self):
        self.assertAlmostEqual(angle_complex(0,0), 0)

    def test_angle_complex_negative(self):
        self.assertAlmostEqual(angle_complex(-1,-1), 5.497787143782138)
        self.assertAlmostEqual(angle_complex(-1,1), 2.3561944901923448)
        self.assertAlmostEqual(angle_complex(-1,2), 0.4636476090008057)
        self.assertAlmostEqual(angle_complex(-1,3), 0.1415926535897931)

    def test_angle_complex_positive(self):
        self.assertAlmostEqual(angle_complex(1,1), 0.7853981633974483)
        self.assertAlmostEqual(angle_complex(1,2), 0.4636476090008057)
        self.assertAlmostEqual(angle_complex(1,3), 0.1415926535897931)
        self.assertAlmostEqual(angle_complex(2,1), 1.1071487179410402)
