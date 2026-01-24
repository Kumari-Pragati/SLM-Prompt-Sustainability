import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(len_complex(3, 4), 5)
        self.assertEqual(len_complex(-3, 4), 5)
        self.assertEqual(len_complex(0, 4), 4)
        self.assertEqual(len_complex(0, -4), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(len_complex(1e-8, 0), 1e-8)
        self.assertEqual(len_complex(-1e-8, 0), 1e-8)
        self.assertEqual(len_complex(0, 1e-8), 1e-8)
        self.assertEqual(len_complex(0, -1e-8), 1e-8)

        self.assertEqual(len_complex(1e20, 0), 1e20)
        self.assertEqual(len_complex(-1e20, 0), 1e20)
        self.assertEqual(len_complex(0, 1e20), 1e20)
        self.assertEqual(len_complex(0, -1e20), 1e20)

    def test_special_cases(self):
        self.assertEqual(len_complex(0, 0), 0)
        self.assertEqual(len_complex(1, 1), 2.23606797749979)
        self.assertEqual(len_complex(-1, 1), 2.23606797749979)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, len_complex, 'a', 'b')
        self.assertRaises(TypeError, len_complex, 3, 'b')
