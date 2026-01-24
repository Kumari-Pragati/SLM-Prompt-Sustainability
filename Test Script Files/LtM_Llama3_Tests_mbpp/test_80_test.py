import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(tetrahedral_number(-1), 0)
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tetrahedral_number('a')
        with self.assertRaises(TypeError):
            tetrahedral_number(None)
