import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)
        self.assertEqual(tetrahedral_number(5), 35)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(-1)

    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(3.5)
