import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 7, 4, 3, 4, 8, 7]
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), 7)

    def test_edge_condition(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        k = 5
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_boundary_condition(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        k = 1
        with self.assertRaises(Exception):
            first_Element(arr, n, k)
