import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([4]), 4)

    def test_list_with_number_and_list(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_list_with_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, 4]], 5]), 15)

    def test_list_with_non_numeric_element(self):
        self.assertEqual(recursive_list_sum(['a', 1, [2, 3]]), 6)
