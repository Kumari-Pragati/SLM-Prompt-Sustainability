import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_recursive_cases(self):
        self.assertEqual(rencontres_number(2, 0), 1)
        self.assertEqual(rencontres_number(3, 0), 2)
        self.assertEqual(rencontres_number(4, 0), 5)

    def test_binomial_coefficient(self):
        self.assertEqual(rencontres_number(3, 1), 3)
        self.assertEqual(rencontres_number(4, 2), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            rencontres_number('a', 0)
        with self.assertRaises(TypeError):
            rencontres_number(0, 'b')
