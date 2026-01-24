import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(last(arr, x, n), 2)

    def test_edge_case_equal(self):
        arr = [1, 2, 3, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(last(arr, x, n), 3)

    def test_edge_case_greater(self):
        arr = [1, 2, 3, 4, 5, 6]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case_smaller(self):
        arr = [1, 2, 3, 4, 5]
        x = 0
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_single_element(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_empty_array(self):
        arr = []
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case_x_not_in_array(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)
