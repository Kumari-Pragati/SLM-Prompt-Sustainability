import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_simple_positive_integers(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)

    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            tetrahedral_number(-1)

    def test_large_numbers(self):
        self.assertEqual(tetrahedral_number(10), 210)
        self.assertEqual(tetrahedral_number(20), 2145)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(1.5)
        with self.assertRaises(TypeError):
            tetrahedral_number('a')
