import unittest
from mbpp_963_code import discriminant_value

class TestDiscriminantValue(unittest.TestCase):

    def test_two_solutions(self):
        self.assertEqual(discriminant_value(1, 2, 1), ("Two solutions", 0))

    def test_one_solution(self):
        self.assertEqual(discriminant_value(1, 2, 1), ("one solution", 0))

    def test_no_real_solution(self):
        self.assertEqual(discriminant_value(1, 1, 1), ("no real solution", -2))
