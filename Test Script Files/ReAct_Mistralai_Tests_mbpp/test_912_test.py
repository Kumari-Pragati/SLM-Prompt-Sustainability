import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_lobb_num_positive_integer(self):
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 2), 5)
        self.assertEqual(lobb_num(3, 3), 14)

    def test_lobb_num_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 1)

    def test_lobb_num_negative_input(self):
        self.assertRaises(ValueError, lobb_num, -1, 1)
        self.assertRaises(ValueError, lobb_num, 1, -1)

    def test_lobb_num_large_input(self):
        self.assertEqual(lobb_num(100, 100), round(1e197, 1))  # Approximately 1e197 for large inputs

    def test_lobb_num_invalid_input(self):
        self.assertRaises(TypeError, lobb_num, 'a', 1)
        self.assertRaises(TypeError, lobb_num, 1, 'a')
