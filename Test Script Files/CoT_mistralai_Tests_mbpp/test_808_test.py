import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_K([], 1))

    def test_single_element_list(self):
        self.assertTrue(check_K([1], 1))
        self.assertFalse(check_K([1], 2))

    def test_multiple_elements_list(self):
        self.assertTrue(check_K([1, 1, 2, 3], 1))
        self.assertFalse(check_K([1, 1, 2, 3], 4))

    def test_negative_numbers(self):
        self.assertTrue(check_K([-1, -2, -3], -1))
        self.assertFalse(check_K([-1, -2, -3], 0))

    def test_floats(self):
        self.assertTrue(check_K([1.0, 2.0, 3.0], 1.0))
        self.assertFalse(check_K([1.0, 2.0, 3.0], 4.0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_K, [1, 2, 3], 'K')
        self.assertRaises(TypeError, check_K, ['1', '2', '3'], 1)
