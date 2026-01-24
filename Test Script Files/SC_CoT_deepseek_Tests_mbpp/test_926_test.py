import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rencontres_number(5, 2), 20)
        self.assertEqual(rencontres_number(3, 1), 3)
        self.assertEqual(rencontres_number(4, 2), 6)

    def test_boundary_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(rencontres_number(0, 1), 0)
        self.assertEqual(rencontres_number(1, 1), 0)
        self.assertEqual(rencontres_number(2, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rencontres_number('5', 2)
        with self.assertRaises(TypeError):
            rencontres_number(5, '2')
        with self.assertRaises(TypeError):
            rencontres_number('5', '2')
        with self.assertRaises(ValueError):
            rencontres_number(-1, 0)
        with self.assertRaises(ValueError):
            rencontres_number(5, -1)
