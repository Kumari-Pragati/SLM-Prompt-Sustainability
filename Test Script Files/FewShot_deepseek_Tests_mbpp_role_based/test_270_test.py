import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = 6
        self.assertEqual(sum_even_and_even_index(arr, n), 6)

    def test_edge_case_with_no_even_numbers(self):
        arr = [1, 3, 5, 7, 9]
        n = 5
        self.assertEqual(sum_even_and_even_index(arr, n), 0)

    def test_boundary_case_with_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(sum_even_and_even_index(arr, n), 0)

    def test_error_handling_with_invalid_input(self):
        arr = [1, 2, 3]
        n = 'a'
        with self.assertRaises(TypeError):
            sum_even_and_even_index(arr, n)
