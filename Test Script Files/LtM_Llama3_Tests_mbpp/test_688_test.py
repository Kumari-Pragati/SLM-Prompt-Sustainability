import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(len_complex(1, 2), 2.23606797749979)
        self.assertEqual(len_complex(-1, 2), 2.23606797749979)
        self.assertEqual(len_complex(1, -2), 2.23606797749979)
        self.assertEqual(len_complex(-1, -2), 2.23606797749979)

    def test_zero(self):
        self.assertEqual(len_complex(0, 0), 0)
        self.assertEqual(len_complex(0, 1), 1)
        self.assertEqual(len_complex(1, 0), 1)
        self.assertEqual(len_complex(1, 1), 1.4142135623730951)

    def test_edge(self):
        self.assertEqual(len_complex(0, float('inf')), float('inf'))
        self.assertEqual(len_complex(0, float('-inf')), float('inf'))
        self.assertEqual(len_complex(float('inf'), 0), float('inf'))
        self.assertEqual(len_complex(float('-inf'), 0), float('inf'))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            len_complex('a', 2)
        with self.assertRaises(TypeError):
            len_complex(1, 'b')
