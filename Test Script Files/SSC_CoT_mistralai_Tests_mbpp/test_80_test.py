import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(tetrahedral_number(1), 0)
        self.assertEqual(tetrahedral_number(2), 1)
        self.assertEqual(tetrahedral_number(3), 4)
        self.assertEqual(tetrahedral_number(4), 10)

    def test_edge_cases(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(-1), -1)
        self.assertEqual(tetrahedral_number(float('inf')), float('inf'))
        self.assertEqual(tetrahedral_number(complex(0, 1)), Complex('0+0j'))

    def test_boundary_cases(self):
        self.assertEqual(tetrahedral_number(1.0), 0)
        self.assertEqual(tetrahedral_number(2.5), 5.5)
        self.assertEqual(tetrahedral_number(-2), 2)
