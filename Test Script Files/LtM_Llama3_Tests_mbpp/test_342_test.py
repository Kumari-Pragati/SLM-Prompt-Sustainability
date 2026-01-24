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

    def test_list_with_duplicates(self):
        self.assertEqual(find_minimum_range([[1, 1, 2]]), (1, 2))

    def test_list_with_negative_numbers(self):
        self.assertEqual(find_minimum_range([[-1, 0, 1]]), (-1, 1))

    def test_list_with_max_value(self):
        self.assertEqual(find_minimum_range([[float('inf')]]), (float('inf'), float('inf')))

    def test_list_with_min_value(self):
        self.assertEqual(find_minimum_range([[float('-inf')]]), (float('-inf'), float('-inf')))

    def test_list_with_max_and_min_values(self):
        self.assertEqual(find_minimum_range([[float('inf'), float('-inf')]]), (float('-inf'), float('inf')))
