import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 0, 4), 9)

    def test_single_element(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_two_elements(self):
        self.assertEqual(find_Max([5, 3], 0, 1), 5)

    def test_decreasing_sequence(self):
        self.assertEqual(find_Max([9, 7, 5, 3, 1], 0, 4), 9)

    def test_increasing_sequence(self):
        self.assertEqual(find_Max([1, 3, 5, 7, 9], 0, 4), 9)

    def test_same_elements(self):
        self.assertEqual(find_Max([5, 5, 5, 5, 5], 0, 4), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_Max([-9, -7, -5, -3, -1], 0, 4), -1)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            find_Max([], 0, -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Max("not an array", 0, 4)
