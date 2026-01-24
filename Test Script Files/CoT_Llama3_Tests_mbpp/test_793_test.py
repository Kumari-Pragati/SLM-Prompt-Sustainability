import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        n = 5
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = 5
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case6(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = 5
        self.assertEqual(last(arr, x, n), 4)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        x = 'a'
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_invalid_input2(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = 'a'
        self.assertEqual(last(arr, x, n), -1)
