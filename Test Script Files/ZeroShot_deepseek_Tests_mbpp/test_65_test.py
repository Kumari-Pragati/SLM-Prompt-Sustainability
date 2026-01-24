import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_nested_list(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], 5]), 15)

    def test_nested_list_with_zero(self):
        self.assertEqual(recursive_list_sum([0, [1, 2], 3]), 6)

    def test_nested_list_with_negative_numbers(self):
        self.assertEqual(recursive_list_sum([1, -2, [3, -4], 5]), 5)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([5]), 5)

    def test_single_nested_list(self):
        self.assertEqual(recursive_list_sum([[5]]), 5)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1, "2", [3, 4], 5])
