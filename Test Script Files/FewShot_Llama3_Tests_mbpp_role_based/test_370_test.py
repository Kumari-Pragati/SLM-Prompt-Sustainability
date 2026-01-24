import unittest
from mbpp_370_code import float_sort

class TestFloatSort(unittest.TestCase):
    def test_typical_use_case(self):
        price = [["apple", "10.0"], ["banana", "5.0"], ["orange", "8.0"]]
        result = float_sort(price)
        self.assertEqual(result, [["orange", "8.0"], ["apple", "10.0"], ["banana", "5.0"]])

    def test_edge_case_empty_list(self):
        price = []
        result = float_sort(price)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        price = [["apple", "10.0"]]
        result = float_sort(price)
        self.assertEqual(result, [["apple", "10.0"]])

    def test_edge_case_all_equal(self):
        price = [["apple", "10.0"], ["banana", "10.0"], ["orange", "10.0"]]
        result = float_sort(price)
        self.assertEqual(result, [["apple", "10.0"], ["banana", "10.0"], ["orange", "10.0"]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            float_sort("not a list")
