import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_list_of_numbers(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_list_of_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4, [5, 6]]), 21)

    def test_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, [3, 4]], 5, [6, [7, 8]]]), 36)

    def test_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, 'a', 2, [3, 4]]), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum('invalid_input')
