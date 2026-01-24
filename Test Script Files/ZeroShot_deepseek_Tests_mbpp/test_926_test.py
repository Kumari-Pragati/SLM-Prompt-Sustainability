import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_zero_n_zero_m(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one_n_zero_m(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_zero_m(self):
        self.assertEqual(rencontres_number(2, 0), 2)

    def test_general_case(self):
        self.assertEqual(rencontres_number(3, 2), 6)
