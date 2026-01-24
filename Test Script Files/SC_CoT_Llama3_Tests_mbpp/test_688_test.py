import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(len_complex(1, 2), 2.23606797749979)
        self.assertEqual(len_complex(-1, 2), 2.23606797749979)
        self.assertEqual(len_complex(1, -2), 2.23606797749979)
        self.assertEqual(len_complex(-1, -2), 2.23606797749979)

    def test_edge_cases(self):
        self.assertEqual(len_complex(0, 0), 0)
        self.assertEqual(len_complex(0, 1), 1)
        self.assertEqual(len_complex(1, 0), 1)
        self.assertEqual(len_complex(-1, 0), 1)

    def test_special_cases(self):
        self.assertEqual(len_complex(0, 1), 1)
        self.assertEqual(len_complex(1, 0), 1)
        self.assertEqual(len_complex(-1, 0), 1)
        self.assertEqual(len_complex(0, -1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            len_complex('a', 2)
        with self.assertRaises(TypeError):
            len_complex(1, 'b')
