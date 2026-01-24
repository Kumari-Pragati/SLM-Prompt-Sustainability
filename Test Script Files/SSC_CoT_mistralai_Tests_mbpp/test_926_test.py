import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(rencontres_number(3, 2), 3)
        self.assertEqual(rencontres_number(4, 3), 4)
        self.assertEqual(rencontres_number(5, 4), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)
        self.assertEqual(rencontres_number(1, 1), 1)
        self.assertEqual(rencontres_number(2, 0), 0)
        self.assertEqual(rencontres_number(2, 2), 2)
        self.assertEqual(rencontres_number(3, 0), 0)
        self.assertEqual(rencontres_number(3, 3), 3)
        self.assertEqual(rencontres_number(4, 0), 0)
        self.assertEqual(rencontres_number(4, 4), 24)

    def test_special_cases(self):
        self.assertEqual(rencontres_number(5, 1), 5)
        self.assertEqual(rencontres_number(6, 2), 15)
        self.assertEqual(rencontres_number(7, 3), 35)
        self.assertEqual(rencontres_number(8, 4), 70)
        self.assertEqual(rencontres_number(9, 5), 126)
