import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 7, 4, 3, 4, 8, 7]
        n = len(arr)
        k = 2
        self.assertEqual(first_Element(arr, n, k), 7)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        k = 5
        self.assertEqual(first_Element(arr, n, k), 1)

    def test_invalid_k(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 0
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_invalid_array(self):
        arr = []
        n = 0
        k = 1
        self.assertEqual(first_Element(arr, n, k), -1)

    def test_no_element_with_k_occurrences(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 6
        self.assertEqual(first_Element(arr, n, k), -1)
