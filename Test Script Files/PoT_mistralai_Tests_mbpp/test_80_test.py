import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(tetrahedral_number(1), 0)
        self.assertEqual(tetrahedral_number(2), 1)
        self.assertEqual(tetrahedral_number(3), 4)
        self.assertEqual(tetrahedral_number(4), 10)
        self.assertEqual(tetrahedral_number(5), 20)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(-1), None)
        self.assertEqual(tetrahedral_number(float('inf')), None)
