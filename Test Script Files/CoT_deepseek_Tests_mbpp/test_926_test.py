import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_zero_n_zero_m(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one_n_zero_m(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_typical_case(self):
        self.assertEqual(rencontres_number(3, 2), 3)

    def test_boundary_case(self):
        self.assertEqual(rencontres_number(10, 0), 90)

    def test_invalid_n(self):
        with self.assertRaises(Exception):
            rencontres_number(-1, 2)

    def test_invalid_m(self):
        with self.assertRaises(Exception):
            rencontres_number(3, -1)

    def test_invalid_n_m(self):
        with self.assertRaises(Exception):
            rencontres_number(-1, -1)
