import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(rencontres_number(3, 2), 3)
        self.assertEqual(rencontres_number(4, 2), 6)
        self.assertEqual(rencontres_number(5, 3), 10)

    def test_boundary_cases(self):
        self.assertEqual(rencontres_number(0, 0), 1)
        self.assertEqual(rencontres_number(1, 0), 0)
        self.assertEqual(rencontres_number(2, 1), 2)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            rencontres_number('3', 2)
        with self.assertRaises(TypeError):
            rencontres_number(3, '2')
        with self.assertRaises(ValueError):
            rencontres_number(-1, 2)
        with self.assertRaises(ValueError):
            rencontres_number(3, -1)
