import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 7
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_edge_case_sum_in_array(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = len(arr)
        sum = 7
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_edge_case_sum_out_of_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_edge_case_sum_equal_to_array_element(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 3
        self.assertEqual(get_pairs_count(arr, n, sum), 1)

    def test_edge_case_sum_equal_to_array_element_with_duplicates(self):
        arr = [1, 2, 3, 3, 4, 5]
        n = len(arr)
        sum = 3
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_invalid_input_non_integer_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum ='seven'
        with self.assertRaises(TypeError):
            get_pairs_count(arr, n, sum)

    def test_invalid_input_negative_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = -7
        with self.assertRaises(TypeError):
            get_pairs_count(arr, n, sum)
