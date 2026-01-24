import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_edge_cases(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 0, 1), 1)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 5, 5), 1)

    def test_empty_list(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)

    def test_single_element_list(self):
        self.assertEqual(count_range_in_list([1], 1, 1), 1)
        self.assertEqual(count_range_in_list([1], 0, 1), 1)
        self.assertEqual(count_range_in_list([1], 1, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_range_in_list("hello", 1, 5)
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3], "hello", 5)
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3], 1, "hello")
