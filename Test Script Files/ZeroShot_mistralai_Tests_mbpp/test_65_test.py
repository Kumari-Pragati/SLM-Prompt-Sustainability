import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([1]), 1)
        self.assertEqual(recursive_list_sum([2]), 2)
        self.assertEqual(recursive_list_sum([3]), 3)

    def test_list_with_multiple_elements(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)
        self.assertEqual(recursive_list_sum([[1], [2], [3]]), 6)

    def test_list_with_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, 4], 5], 6]), 23)
        self.assertEqual(recursive_list_sum([[1], [[2], [3]], [4]]), 10)
