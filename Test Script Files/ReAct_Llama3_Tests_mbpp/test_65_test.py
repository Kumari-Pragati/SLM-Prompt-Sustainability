import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_mixed_type_list(self):
        self.assertEqual(recursive_list_sum([1, 'a', [2, 3], 4]), 10)

    def test_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1, 'a', [2, 3, 'b'], 4])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1, 'a', 2, 4])
