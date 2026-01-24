import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        n = len(arr)
        self.assertEqual(last(arr, x, n), 3)

    def test_edge_case_not_found(self):
        arr = [1, 3, 5, 7, 9]
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case_empty_array(self):
        arr = []
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case_single_element(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_duplicates(self):
        arr = [1, 3, 5, 7, 7, 9]
        x = 7
        n = len(arr)
        self.assertEqual(last(arr, x, n), 5)
