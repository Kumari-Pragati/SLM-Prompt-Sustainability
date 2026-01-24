import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_zero_zero(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one_zero(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_zero_nonzero(self):
        self.assertEqual(rencontres_number(0, 1), 0)

    def test_nonzero_zero(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_nonzero_nonzero(self):
        self.assertEqual(rencontres_number(2, 1), 1)

    def test_high_n_zero(self):
        self.assertEqual(rencontres_number(10, 0), 0)

    def test_high_n_nonzero(self):
        self.assertEqual(rencontres_number(10, 5), 10)

    def test_high_m_high_n(self):
        self.assertEqual(rencontres_number(10, 5), 10)

    def test_high_m_low_n(self):
        self.assertEqual(rencontres_number(5, 3), 10)
