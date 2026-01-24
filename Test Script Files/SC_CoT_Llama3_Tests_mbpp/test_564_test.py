import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 4)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_edge_case_two_element_array(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 1)

    def test_edge_case_duplicates(self):
        arr = [1, 2, 2, 3, 3, 3]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 3)

    def test_invalid_input_non_integer(self):
        arr = [1, 2, 3]
        n ='string'
        with self.assertRaises(TypeError):
            count_Pairs(arr, n)

    def test_invalid_input_negative_integer(self):
        arr = [1, 2, 3]
        n = -1
        with self.assertRaises(TypeError):
            count_Pairs(arr, n)
