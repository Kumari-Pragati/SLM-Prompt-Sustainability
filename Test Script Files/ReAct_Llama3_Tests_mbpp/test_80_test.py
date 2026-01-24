import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_one(self):
        self.assertEqual(tetrahedral_number(1), 1)

    def test_small_positive(self):
        self.assertEqual(tetrahedral_number(2), 4)

    def test_large_positive(self):
        self.assertEqual(tetrahedral_number(10), 385)

    def test_negative(self):
        with self.assertRaises(ZeroDivisionError):
            tetrahedral_number(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(2.5)
