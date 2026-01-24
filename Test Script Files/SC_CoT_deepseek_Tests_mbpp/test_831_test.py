import unittest
from mbpp_831_code import count_Pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 2, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 2)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_corner_case_repeated_elements(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 6)

    def test_corner_case_unique_elements(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_invalid_input_negative_elements(self):
        arr = [-1, 2, 3, 2, -1]
        n = len(arr)
        with self.assertRaises(Exception):
            count_Pairs(arr, n)

    def test_invalid_input_non_integer_elements(self):
        arr = [1, 'two', 3, 'two', 1]
        n = len(arr)
        with self.assertRaises(Exception):
            count_Pairs(arr, n)
