import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(len_complex(1, 1), cmath.sqrt(2))
        self.assertAlmostEqual(len_complex(0, 0), 0)
        self.assertAlmostEqual(len_complex(3, 4), 5)

    def test_edge_conditions(self):
        self.assertAlmostEqual(len_complex(0, 1), 1)
        self.assertAlmostEqual(len_complex(1, 0), 1)
        self.assertAlmostEqual(len_complex(-1, 0), 1)
        self.assertAlmostEqual(len_complex(0, -1), 1)

    def test_complex_cases(self):
        self.assertAlmostEqual(len_complex(-1, -1), cmath.sqrt(2))
        self.assertAlmostEqual(len_complex(100, 100), cmath.sqrt(20000))
        self.assertAlmostEqual(len_complex(-100, -100), cmath.sqrt(20000))
