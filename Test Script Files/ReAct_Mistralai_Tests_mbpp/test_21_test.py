import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiples_of_num(5, 3), [3, 6, 9, 12, 15])
        self.assertEqual(multiples_of_num(10, 2), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_zero_and_negative_numbers(self):
        self.assertEqual(multiples_of_num(0, 4), [])
        self.assertEqual(multiples_of_num(-3, 2), [-2, -4])
        self.assertEqual(multiples_of_num(-5, -3), [3, 0, -3, 6])

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            multiples_of_num(5)

    def test_negative_m(self):
        self.assertEqual(multiples_of_num(-5, 3), [-3, -6, -9, -12, -15])

    def test_n_is_zero(self):
        self.assertEqual(multiples_of_num(5, 0), [])
