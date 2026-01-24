import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_list_of_numbers(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_list_of_lists(self):
        self.assertEqual(recursive_list_sum([[1, 2], [3, 4]]), 10)

    def test_list_of_lists_of_lists(self):
        self.assertEqual(recursive_list_sum([[[1]]]), 1)

    def test_list_of_strings(self):
        self.assertEqual(recursive_list_sum(["a", "b", "c"]), 0)

    def test_list_of_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], "a", 4]), 10)
