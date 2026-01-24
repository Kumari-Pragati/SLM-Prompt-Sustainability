import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_tetrahedral_number(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)
        self.assertEqual(tetrahedral_number(5), 35)
        self.assertEqual(tetrahedral_number(6), 56)
        self.assertEqual(tetrahedral_number(7), 84)
        self.assertEqual(tetrahedral_number(8), 120)
        self.assertEqual(tetrahedral_number(9), 165)
        self.assertEqual(tetrahedral_number(10), 220)

    def test_tetrahedral_number_edge_cases(self):
        self.assertRaises(TypeError, tetrahedral_number, 'a')
        self.assertRaises(TypeError, tetrahedral_number, None)
