import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(tetrahedral_number(1), 0)
        self.assertEqual(tetrahedral_number(2), 1)
        self.assertEqual(tetrahedral_number(3), 4)
        self.assertEqual(tetrahedral_number(4), 10)
        self.assertEqual(tetrahedral_number(5), 20)

    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_negative_integer(self):
        self.assertEqual(tetrahedral_number(-1), -1/6)
        self.assertEqual(tetrahedral_number(-2), -2/3)
        self.assertEqual(tetrahedral_number(-3), -14/3)
