import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)
        self.assertAlmostEqual(angle_complex(2, 2), 1.1071487179413806)
        self.assertAlmostEqual(angle_complex(3, 3), 1.1071487179413806)

    def test_edge_cases(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), 1.5707963267948966)
        self.assertAlmostEqual(angle_complex(1, 0), 0.7853981633974483)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 1)
        with self.assertRaises(TypeError):
            angle_complex(1, 'b')
