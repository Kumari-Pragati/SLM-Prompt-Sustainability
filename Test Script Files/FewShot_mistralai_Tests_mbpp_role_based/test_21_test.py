import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiples_of_num(4, 2), [2, 4, 6, 8])
        self.assertEqual(multiples_of_num(6, 3), [3, 6, 9])

    def test_zero(self):
        self.assertEqual(multiples_of_num(0, 0), [])
        self.assertEqual(multiples_of_num(0, 1), [0])

    def test_negative_numbers(self):
        self.assertEqual(multiples_of_num(-3, -2), [-2, 0, 2, 4])
        self.assertEqual(multiples_of_num(-5, -3), [-3, 0, 3, 6])

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            multiples_of_num(0, 0)
