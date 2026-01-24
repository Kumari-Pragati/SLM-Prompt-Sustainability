import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(len_complex(3,4), 5.0)
        self.assertEqual(len_complex(-3,4), 5.0)
        self.assertEqual(len_complex(3,-4), 5.0)
        self.assertEqual(len_complex(-3,-4), 5.0)

    def test_edge(self):
        self.assertEqual(len_complex(0,0), 0.0)
        self.assertEqual(len_complex(0,1), 1.0)
        self.assertEqual(len_complex(1,0), 1.0)
        self.assertEqual(len_complex(1,1), 1.4142135623730951)

    def test_boundary(self):
        self.assertEqual(len_complex(1,1), 1.4142135623730951)
        self.assertEqual(len_complex(-1,1), 1.4142135623730951)
        self.assertEqual(len_complex(1,-1), 1.4142135623730951)
        self.assertEqual(len_complex(-1,-1), 1.4142135623730951)
