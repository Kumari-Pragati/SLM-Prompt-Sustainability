import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rencontres_number(3, 2), 3)
        self.assertEqual(rencontres_number(4, 1), 12)
        self.assertEqual(rencontres_number(5, 3), 45)

    def test_edge_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(rencontres_number(2, 0), 2)
        self.assertEqual(rencontres_number(2, 1), 2)
        self.assertEqual(rencontres_number(3, 0), 6)
        self.assertEqual(rencontres_number(3, 1), 6)
        self.assertEqual(rencontres_number(3, 2), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            rencontres_number(-1, 2)
        with self.assertRaises(Exception):
            rencontres_number(2, -1)
        with self.assertRaises(Exception):
            rencontres_number(2, 3)
