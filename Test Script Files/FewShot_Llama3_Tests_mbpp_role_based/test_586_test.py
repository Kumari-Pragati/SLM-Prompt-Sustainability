import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 5
        k = 3
        result = split_Arr(a, n, k)
        expected_result = [a[3:], a[:3]]
        self.assertEqual(result, expected_result)

    def test_edge_case_n_equal_k(self):
        a = [1, 2, 3, 4, 5]
        n = 2
        k = 2
        result = split_Arr(a, n, k)
        expected_result = [[a[2:]], a[:2]]
        self.assertEqual(result, expected_result)

    def test_edge_case_n_greater_than_k(self):
        a = [1, 2, 3, 4, 5]
        n = 5
        k = 2
        result = split_Arr(a, n, k)
        expected_result = [[a[2:]], a[:2]]
        self.assertEqual(result, expected_result)

    def test_edge_case_k_greater_than_n(self):
        a = [1, 2, 3, 4, 5]
        n = 2
        k = 5
        result = split_Arr(a, n, k)
        expected_result = [[a[2:]], a[:2]]
        self.assertEqual(result, expected_result)

    def test_invalid_input_type_a(self):
        a = 'hello'
        n = 2
        k = 1
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

    def test_invalid_input_type_n(self):
        a = [1, 2, 3, 4, 5]
        n = 'hello'
        k = 1
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)

    def test_invalid_input_type_k(self):
        a = [1, 2, 3, 4, 5]
        n = 2
        k = 'hello'
        with self.assertRaises(TypeError):
            split_Arr(a, n, k)
