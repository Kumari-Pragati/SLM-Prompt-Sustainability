import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tetrahedral_number(3), 6)

    def test_edge_case(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)

    def test_boundary_case(self):
        self.assertEqual(tetrahedral_number(3), 6)
        self.assertEqual(tetrahedral_number(4), 10)
        self.assertEqual(tetrahedral_number(5), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tetrahedral_number('a')
