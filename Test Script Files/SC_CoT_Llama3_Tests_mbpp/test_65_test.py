import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4, [5, 6]]), 21)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([10]), 10)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum("hello")

    def test_mixed_type_list(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    def test_list_with_negative_numbers(self):
        self.assertEqual(recursive_list_sum([-1, -2, -3, -4, -5]), -15)

    def test_list_with_zero(self):
        self.assertEqual(recursive_list_sum([0, 1, 2, 3, 4, 5]), 15)
