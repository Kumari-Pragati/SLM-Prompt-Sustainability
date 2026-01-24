import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        k = 10
        self.assertEqual(no_of_subsequences(arr, k), 6)

    def test_boundary_case(self):
        arr = [1, 2, 3, 4]
        k = 0
        self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_edge_case(self):
        arr = [1, 2, 3, 4]
        k = 1
        self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        k = -1
        with self.assertRaises(Exception):
            no_of_subsequences(arr, k)

    def test_empty_array(self):
        arr = []
        k = 10
        self.assertEqual(no_of_subsequences(arr, k), 1)
