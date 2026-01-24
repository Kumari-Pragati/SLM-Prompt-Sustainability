import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(lobb_num(1, 1), 1)
        self.assertEqual(lobb_num(2, 2), 3)
        self.assertEqual(lobb_num(3, 3), 11)

    def test_negative_input(self):
        self.assertRaises(ValueError, lobb_num, -1, 1)
        self.assertRaises(ValueError, lobb_num, 1, -1)

    def test_zero_input(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 0)
        self.assertEqual(lobb_num(1, 0), 1)

    def test_large_input(self):
        self.assertRaises(ValueError, lobb_num, 100, 100)
