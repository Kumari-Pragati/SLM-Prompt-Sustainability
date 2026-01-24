import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, "two", 3.0, [4, 5]]), 14.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum("not a list")
