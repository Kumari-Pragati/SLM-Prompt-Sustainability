import unittest
from mbpp_506_code import permutation_coefficient

class TestPermutationCoefficient(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(permutation_coefficient(3, 2), 2)
        self.assertEqual(permutation_coefficient(4, 2), 6)

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertEqual(permutation_coefficient(0, 0), 1)
        self.assertEqual(permutation_coefficient(1, 0), 1)
        self.assertEqual(permutation_coefficient(2, 1), 2)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(permutation_coefficient(5, 3), 20)
        self.assertEqual(permutation_coefficient(6, 4), 30)
