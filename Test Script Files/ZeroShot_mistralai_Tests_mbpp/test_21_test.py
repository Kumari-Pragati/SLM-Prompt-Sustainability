import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_multiples_of_num_positive(self):
        self.assertEqual(multiples_of_num(3, 5), [15, 10, 5])
        self.assertEqual(multiples_of_num(4, 2), [8, 4])
        self.assertEqual(multiples_of_num(6, 3), [18, 15, 12, 9])

    def test_multiples_of_num_zero(self):
        self.assertEqual(multiples_of_num(0, 4), [])

    def test_multiples_of_num_negative(self):
        self.assertEqual(multiples_of_num(-3, 5), [])
        self.assertEqual(multiples_of_num(-4, -2), [-8, -6, -4])

    def test_multiples_of_num_same(self):
        self.assertEqual(multiples_of_num(5, 5), [25])
