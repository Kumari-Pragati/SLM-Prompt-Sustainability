import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)

    def test_boundary_conditions(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(1), 1)

    def test_edge_cases(self):
        self.assertEqual(tetrahedral_number(5), 55)
        self.assertEqual(tetrahedral_number(10), 210)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tetrahedral_number("a")
        with self.assertRaises(TypeError):
            tetrahedral_number(None)
        with self.assertRaises(TypeError):
            tetrahedral_number([1, 2, 3])
