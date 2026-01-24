import unittest
from mbpp_926_code import rencontres_number, binomial_coeffi

class TestRencontresNumber(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_edge_case(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_recursive_case(self):
        self.assertEqual(rencontres_number(2, 0), 1)

    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coeffi(3, 1), 3)

    def test_binomial_coefficient_edge_case(self):
        self.assertEqual(binomial_coeffi(3, 0), 1)
        self.assertEqual(binomial_coeffi(3, 3), 1)

    def test_binomial_coefficient_recursive_case(self):
        self.assertEqual(binomial_coeffi(4, 2), 6)

    def test_binomial_coefficient_recursive_case_edge(self):
        self.assertEqual(binomial_coeffi(4, 0), 1)
        self.assertEqual(binomial_coeffi(4, 4), 1)
