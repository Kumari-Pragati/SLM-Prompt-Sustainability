import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_rencontres_number_base_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)
        self.assertEqual(rencontres_number(2, 0), 2)
        self.assertEqual(rencontres_number(3, 0), 6)
        self.assertEqual(rencontres_number(4, 0), 24)

    def test_rencontres_number_with_m_greater_than_zero(self):
        self.assertEqual(rencontres_number(5, 2), 15)
        self.assertEqual(rencontres_number(6, 3), 45)
        self.assertEqual(rencontres_number(7, 4), 105)
        self.assertEqual(rencontres_number(8, 5), 210)
        self.assertEqual(rencontres_number(9, 6), 330)

    def test_rencontres_number_with_n_greater_than_m(self):
        self.assertEqual(rencontres_number(5, 3), 10)
        self.assertEqual(rencontres_number(6, 4), 15)
        self.assertEqual(rencontres_number(7, 5), 21)
        self.assertEqual(rencontres_number(8, 6), 28)
        self.assertEqual(rencontres_number(9, 7), 36)
