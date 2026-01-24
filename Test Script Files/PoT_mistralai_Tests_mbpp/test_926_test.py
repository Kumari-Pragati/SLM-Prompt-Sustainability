import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)
        self.assertEqual(rencontres_number(2, 0), 2)
        self.assertEqual(rencontres_number(2, 1), 2)
        self.assertEqual(rencontres_number(2, 2), 1)
        self.assertEqual(rencontres_number(3, 1), 3)
        self.assertEqual(rencontres_number(3, 2), 3)
        self.assertEqual(rencontres_number(3, 3), 1)

    def test_edge_cases(self):
        self.assertEqual(rencontres_number(-1, 0), None)
        self.assertEqual(rencontres_number(0, -1), None)
        self.assertEqual(rencontres_number(1, -1), None)
        self.assertEqual(rencontres_number(0, 2), 0)
        self.assertEqual(rencontres_number(1, 2), 1)
        self.assertEqual(rencontres_number(2, 3), 2)
        self.assertEqual(rencontres_number(3, 4), 6)
