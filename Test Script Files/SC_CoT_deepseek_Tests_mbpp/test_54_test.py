import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_edge_case_single_element(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_edge_case_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_edge_case_max_value(self):
        self.assertEqual(counting_sort([1000, 999, 998, 997]), [997, 998, 999, 1000])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            counting_sort([1, 'a', 2])

    def test_invalid_input_negative_number(self):
        with self.assertRaises(ValueError):
            counting_sort([1, -1, 2])
