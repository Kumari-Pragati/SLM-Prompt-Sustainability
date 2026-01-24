import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_one(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_zero_m(self):
        self.assertEqual(rencontres_number(2, 0), 1)

    def test_binomial_coeffi(self):
        self.assertEqual(rencontres_number(2, 1), 2)

    def test_recursive(self):
        self.assertEqual(rencontres_number(3, 1), 2)

    def test_edge_case(self):
        self.assertEqual(rencontres_number(10, 5), 252)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rencontres_number('a', 0)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            rencontres_number(0, 'b')
