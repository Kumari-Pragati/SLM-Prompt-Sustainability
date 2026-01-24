import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):
    def test_empty_range(self):
        self.assertListEqual(multiples_of_num(1, 1), [])

    def test_single_multiple(self):
        self.assertListEqual(multiples_of_num(3, 6), [3])

    def test_multiple_values(self):
        self.assertListEqual(multiples_of_num(5, 15), [5, 10, 15])

    def test_large_range(self):
        self.assertListEqual(multiples_of_num(10, 100), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    def test_negative_numbers(self):
        self.assertListEqual(multiples_of_num(-3, 9), [-3, 6, 9])

    def test_zero_as_n(self):
        self.assertListEqual(multiples_of_num(3, 0), [])

    def test_zero_as_m(self):
        self.assertListEqual(multiples_of_num(0, 6), [0, 6])

    def test_m_greater_than_n(self):
        self.assertListEqual(multiples_of_num(5, 3), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, multiples_of_num, "a", 3)
        self.assertRaises(TypeError, multiples_of_num, 3, "a")
