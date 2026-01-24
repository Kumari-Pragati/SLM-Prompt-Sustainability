import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_positive_numbers(self):
        test_list = [([1, 2, 3], 1), ([[-1, 0, 1], 2), ([[5, 10, 15], 3)]
        self.assertEqual(add_K_element(test_list, 1),
                         [([2, 3, 4], 1), ([[-2, 0, 3], 2), ([[6, 13, 18], 3)]

    def test_zero(self):
        test_list = [([0, 0, 0], 0), ([[-1, 0, 0], 0), ([[0, 0, 0], 0)]
        self.assertEqual(add_K_element(test_list, 0),
                         [([0, 0, 0], 0), ([[-1, 0, 0], 0), ([[0, 0, 0], 0)]

    def test_negative_numbers(self):
        test_list = [([-1, -2, -3], -1), ([[-5, -10, -15], -3)]
        self.assertEqual(add_K_element(test_list, -1),
                         [([0, -1, -2], -1), ([[-6, -13, -18], -3)]

    def test_empty_list(self):
        self.assertRaises(ValueError, add_K_element, [])

    def test_list_with_single_element(self):
        self.assertRaises(ValueError, add_K_element, [([1], 2)]

    def test_K_is_not_an_integer(self):
        self.assertRaises(TypeError, add_K_element, [([1, 2, 3], 'K')]
