import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(find_Max([5], 0, 0), 5)

    def test_empty_array(self):
        self.assertEqual(find_Max([], 0, 0), None)

    def test_ascending_array(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_descending_array(self):
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)

    def test_array_with_duplicates(self):
        self.assertEqual(find_Max([1, 1, 2, 3, 4, 4, 5], 0, 6), 5)

    def test_negative_numbers_array(self):
        self.assertEqual(find_Max([-5, -4, -3, -2, -1], 0, 4), -1)

    def test_array_with_zero(self):
        self.assertEqual(find_Max([0, 1, 2, 3, 4], 0, 4), 4)

    def test_array_with_negative_zero(self):
        self.assertEqual(find_Max([0, -1, -2, -3, -4], 0, 4), -4)

    def test_array_with_large_numbers(self):
        self.assertEqual(find_Max([1000000000, 999999999, 999999998, 999999997, 999999996], 0, 4), 1000000000)
