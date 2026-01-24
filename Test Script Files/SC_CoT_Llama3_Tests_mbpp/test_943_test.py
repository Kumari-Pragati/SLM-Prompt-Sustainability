import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):
    def test_typical_inputs(self):
        num1 = [1, 2, 3]
        num2 = [4, 5, 6]
        result = combine_lists(num1, num2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        num1 = []
        num2 = [4, 5, 6]
        result = combine_lists(num1, num2)
        self.assertEqual(result, [4, 5, 6])

    def test_edge_case_single_list(self):
        num1 = [1, 2, 3]
        num2 = []
        result = combine_lists(num1, num2)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_equal_length_lists(self):
        num1 = [1, 2, 3]
        num2 = [4, 5, 6]
        result = combine_lists(num1, num2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_edge_case_reverse_order(self):
        num1 = [6, 5, 4]
        num2 = [3, 2, 1]
        result = combine_lists(num1, num2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_invalid_input_type(self):
        num1 = "hello"
        num2 = [4, 5, 6]
        with self.assertRaises(TypeError):
            combine_lists(num1, num2)

    def test_invalid_input_non_iterable(self):
        num1 = 123
        num2 = [4, 5, 6]
        with self.assertRaises(TypeError):
            combine_lists(num1, num2)
