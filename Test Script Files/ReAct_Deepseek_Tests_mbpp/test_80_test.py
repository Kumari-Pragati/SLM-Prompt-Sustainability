import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)

    def test_edge_cases(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(10), 210)
        self.assertEqual(tetrahedral_number(100), 505050)

    def test_negative_cases(self):
        with self.assertRaises(TypeError):
            tetrahedral_number(-1)
        with self.assertRaises(TypeError):
            tetrahedral_number('a')
