import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(len_complex(1, 0), 1)
        self.assertEqual(len_complex(0, 1), 1)
        self.assertEqual(len_complex(1, 1), 2)

    def test_simple_negative(self):
        self.assertEqual(len_complex(-1, 0), 1)
        self.assertEqual(len_complex(0, -1), 1)
        self.assertEqual(len_complex(-1, -1), 2)

    def test_edge_zero(self):
        self.assertEqual(len_complex(0, 0), 0)

    def test_edge_max_abs(self):
        self.assertEqual(len_complex(1e100, 0), 1e100)
        self.assertEqual(len_complex(0, 1e100), 1e100)

    def test_complex_input(self):
        self.assertEqual(len_complex(1+2j, 3-4j), 5)
