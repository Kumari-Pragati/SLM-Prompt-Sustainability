import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_zero_and_zero(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one_and_zero(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_zero_and_nonzero(self):
        self.assertEqual(rencontres_number(0, 1), 0)

    def test_nonzero_and_zero(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_nonzero_and_nonzero(self):
        self.assertEqual(rencontres_number(2, 1), 1)

    def test_nonzero_and_nonzero_edge(self):
        self.assertEqual(rencontres_number(2, 2), 1)

    def test_nonzero_and_nonzero_high(self):
        self.assertEqual(rencontres_number(5, 3), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rencontres_number('a', 1)
