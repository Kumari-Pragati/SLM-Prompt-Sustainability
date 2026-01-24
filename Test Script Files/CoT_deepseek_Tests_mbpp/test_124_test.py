import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)
        self.assertAlmostEqual(angle_complex(1, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), 1.5707963267948966)

    def test_edge_cases(self):
        self.assertAlmostEqual(angle_complex(-1, 0), 3.141592653589793)
        self.assertAlmostEqual(angle_complex(0, -1), -1.5707963267948966)
        self.assertAlmostEqual(angle_complex(-1, -1), -0.7853981633974483)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex("1", 1)
        with self.assertRaises(TypeError):
            angle_complex(1, "1")
        with self.assertRaises(TypeError):
            angle_complex("1", "1")
