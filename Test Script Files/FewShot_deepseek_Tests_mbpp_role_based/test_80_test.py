import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tetrahedral_number(5), 35)

    def test_zero(self):
        self.assertEqual(tetrahedral_number(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            tetrahedral_number(-1)

    def test_boundary_conditions(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
