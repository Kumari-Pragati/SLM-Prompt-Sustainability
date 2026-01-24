import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertTrue(check(arr, n))

    def test_edge_case_decreasing(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertFalse(check(arr, n))

    def test_edge_case_increasing(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertTrue(check(arr, n))

    def test_edge_case_constant(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertTrue(check(arr, n))

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertTrue(check(arr, n))

    def test_edge_case_empty(self):
        arr = []
        n = len(arr)
        self.assertTrue(check(arr, n))

    def test_error_case_non_integer(self):
        arr = [1, 2, 3, 4, 5]
        n = 'five'
        with self.assertRaises(TypeError):
            check(arr, n)

    def test_error_case_non_list(self):
        arr = 'hello'
        n = 5
        with self.assertRaises(TypeError):
            check(arr, n)
