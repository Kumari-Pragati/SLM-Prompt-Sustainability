import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(len_complex(3, 4), 5)
        self.assertEqual(len_complex(-3, 4), 5)
        self.assertEqual(len_complex(3, -4), 5)
        self.assertEqual(len_complex(-3, -4), 5)

    def test_edge_case_zero(self):
        self.assertEqual(len_complex(0, 0), 0)
        self.assertEqual(len_complex(-0, 0), 0)
        self.assertEqual(len_complex(0, -0), 0)

    def test_edge_case_one(self):
        self.assertEqual(len_complex(1, 0), 1)
        self.assertEqual(len_complex(-1, 0), 1)

    def test_edge_case_negative_one(self):
        self.assertEqual(len_complex(-1, 0), 1)

    def test_edge_case_imaginary(self):
        self.assertEqual(len_complex(0, 1), 1)
        self.assertEqual(len_complex(0, -1), 1)
