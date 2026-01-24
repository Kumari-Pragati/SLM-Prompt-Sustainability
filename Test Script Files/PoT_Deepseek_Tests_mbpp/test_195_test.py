import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_case_not_found(self):
        arr = [1, 3, 5, 7, 9]
        x = 10
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_boundary_case_empty_array(self):
        arr = []
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_corner_case_duplicate_elements(self):
        arr = [1, 3, 5, 5, 7, 9]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_corner_case_single_element(self):
        arr = [5]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)
