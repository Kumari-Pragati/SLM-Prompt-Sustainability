import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_minimum_range([]), (float('-inf'), float('inf')))

    def test_single_element_list(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_two_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2]]), (1, 2))

    def test_three_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3]]), (1, 3))

    def test_four_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4]]), (1, 4))

    def test_five_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5]]), (1, 5))

    def test_six_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5, 6]]), (1, 6))

    def test_seven_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5, 6, 7]]), (1, 7))

    def test_eight_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5, 6, 7, 8]]), (1, 8))

    def test_nine_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5, 6, 7, 8, 9]]), (1, 9))

    def test_ten_element_list(self):
        self.assertEqual(find_minimum_range([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), (1, 10))

    def test_list_with_duplicates(self):
        self.assertEqual(find_minimum_range([[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]]), (1, 5))

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_minimum_range([[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]), (-10, -1))

    def test_list_with_positive_and_negative_numbers(self):
        self.assertEqual(find_minimum_range([[1, -2, 3, -4, 5, -6, 7, -8, 9, -10]]), (-10, 9))
