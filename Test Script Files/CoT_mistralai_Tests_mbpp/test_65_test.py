import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)
        self.assertEqual(recursive_list_sum([-1]), -1)
        self.assertEqual(recursive_list_sum([0]), 0)

    def test_multiple_elements(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)
        self.assertEqual(recursive_list_sum([-1, -2, -3]), -6)
        self.assertEqual(recursive_list_sum([0, 1, 2, 3]), 6)

    def test_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)
        self.assertEqual(recursive_list_sum([[1], [2], [3]]), 6)
        self.assertEqual(recursive_list_sum([[1], [2, 3], [4, 5, 6]]), 21)

    def test_empty_nested_list(self):
        self.assertEqual(recursive_list_sum([[1], [], [3]]), 4)

    def test_invalid_input(self):
        self.assertRaises(TypeError, recursive_list_sum, 123)
        self.assertRaises(TypeError, recursive_list_sum, (1, 2, 3))
