import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 7
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)

    def test_edge_case_sum_in_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)

    def test_edge_case_sum_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_edge_case_single_element_array(self):
        arr = [1]
        n = len(arr)
        sum = 1
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        sum = 1
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_invalid_input_non_integer_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum ='seven'
        with self.assertRaises(TypeError):
            get_Pairs_Count(arr, n, sum)

    def test_invalid_input_non_integer_n(self):
        arr = [1, 2, 3, 4, 5]
        n = 'five'
        sum = 7
        with self.assertRaises(TypeError):
            get_Pairs_Count(arr, n, sum)

    def test_invalid_input_non_integer_arr(self):
        arr = 'one two three four five'
        n = len(arr)
        sum = 7
        with self.assertRaises(TypeError):
            get_Pairs_Count(arr, n, sum)
