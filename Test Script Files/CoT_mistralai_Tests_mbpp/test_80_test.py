import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_tetrahedral_number_positive_integer(self):
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

    def test_tetrahedral_number_large_integer(self):
        self.assertEqual(tetrahedral_number(100), 327600)
        self.assertEqual(tetrahedral_number(200), 8417280)
        self.assertEqual(tetrahedral_number(300), 232660480)

    def test_tetrahedral_number_zero(self):
        self.assertEqual(tetrahedral_number(-1), None)
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1.5), None)
        self.assertEqual(tetrahedral_number(-2.3), None)
        self.assertEqual(tetrahedral_number('abc'), None)
