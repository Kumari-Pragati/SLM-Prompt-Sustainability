import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_num_keith(9101))
        self.assertTrue(is_num_keith(12345))
        self.assertTrue(is_num_keith(987654321))

    def test_zero(self):
        self.assertTrue(is_num_keith(0))

    def test_negative_numbers(self):
        self.assertFalse(is_num_keith(-1))
        self.assertFalse(is_num_keith(-9101))
        self.assertFalse(is_num_keith(-987654321))

    def test_single_digit_numbers(self):
        self.assertTrue(is_num_keith(0))
        self.assertTrue(is_num_keith(1))
        self.assertTrue(is_num_keith(2))
        self.assertTrue(is_num_keith(3))
        self.assertTrue(is_num_keith(4))
        self.assertTrue(is_num_keith(5))
        self.assertTrue(is_num_keith(6))
        self.assertTrue(is_num_keith(7))
        self.assertTrue(is_num_keith(8))
        self.assertTrue(is_num_keith(9))

    def test_edge_cases(self):
        self.assertTrue(is_num_keith(10**100))
        self.assertTrue(is_num_keith(10**100 - 1))
        self.assertFalse(is_num_keith(10**100 + 1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_num_keith, 'not_a_number')
        self.assertRaises(TypeError, is_num_keith, None)
        self.assertRaises(TypeError, is_num_keith, [1, 2, 3])
        self.assertRaises(TypeError, is_num_keith, (1, 2, 3))
        self.assertRaises(TypeError, is_num_keith, {1: 2, 3: 4})
        self.assertRaises(TypeError, is_num_keith, (1,))
        self.assertRaises(TypeError, is_num_keith, {})
