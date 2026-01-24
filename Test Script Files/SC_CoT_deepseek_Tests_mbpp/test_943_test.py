import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_typical_case(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(combine_lists(num1, num2), expected_output)

    def test_empty_lists(self):
        num1 = []
        num2 = []
        expected_output = []
        self.assertEqual(combine_lists(num1, num2), expected_output)

    def test_one_empty_list(self):
        num1 = [1, 2, 3]
        num2 = []
        expected_output = [1, 2, 3]
        self.assertEqual(combine_lists(num1, num2), expected_output)

    def test_sorted_lists(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(combine_lists(num1, num2), expected_output)

    def test_unsorted_lists(self):
        num1 = [5, 3, 1]
        num2 = [6, 4, 2]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(combine_lists(num1, num2), expected_output)

    def test_duplicate_elements(self):
        num1 = [1, 2, 2]
        num2 = [2, 3, 4]
        expected_output = [1, 2, 2, 2, 3, 4]
        self.assertEqual(combine_lists(num1, num2), expected_output)
