import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, 'a', [2, 3], 4]), 10)

    def test_empty_list_nested(self):
        self.assertEqual(recursive_list_sum([1, [], 2, [3, 4]]), 10)

    def test_empty_list_nested_multiple(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, 4]], 5, [6, 7]]), 18)
