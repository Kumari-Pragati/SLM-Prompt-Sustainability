import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(tetrahedral_number(1), 1)
        self.assertEqual(tetrahedral_number(2), 4)
        self.assertEqual(tetrahedral_number(3), 10)
        self.assertEqual(tetrahedral_number(4), 20)
        self.assertEqual(tetrahedral_number(5), 35)

    def test_edge_cases(self):
        self.assertEqual(tetrahedral_number(0), 0)
        self.assertEqual(tetrahedral_number(-1), 0)
        self.assertEqual(tetrahedral_number(1.5), 2.5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            tetrahedral_number('a')
        with self.assertRaises(TypeError):
            tetrahedral_number(None)

    def test_large_inputs(self):
        self.assertEqual(tetrahedral_number(100), 362880)
