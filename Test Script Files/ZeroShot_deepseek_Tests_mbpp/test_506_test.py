import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    def test_permutation_coefficient(self):
        self.assertEqual(permutation_coefficient(3, 2), 2)
        self.assertEqual(permutation_coefficient(4, 2), 6)
        self.assertEqual(permutation_coefficient(5, 3), 20)
        self.assertEqual(permutation_coefficient(6, 4), 60)
        self.assertEqual(permutation_coefficient(7, 5), 140)
