import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_integer(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_single_list(self):
        self.assertEqual(recursive_list_sum([[2]]), 2)

    def test_multiple_integers(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_multiple_lists(self):
        self.assertEqual(recursive_list_sum([[1], [2], [3]]), 6)

    def test_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, "two", [3]]), 6)

    def test_nested_lists(self):
        self.assertEqual(recursive_list_sum([[1], [2, [3]], [4]]), 10)

    def test_large_list(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(recursive_list_sum(large_list), sum(large_list))

    def test_empty_list_in_nested_list(self):
        self.assertEqual(recursive_list_sum([[], 1, [2]]), 3)

    def test_list_with_non_numeric_element(self):
        self.assertEqual(recursive_list_sum([1, "not a number"]), TypeError)
