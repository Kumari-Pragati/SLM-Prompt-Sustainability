import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 0
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 5
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 6
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = -1
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 6.5
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case6(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = -0.5
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case7(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 0.5
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case8(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1.5
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case9(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 2.5
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case10(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 3.5
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case11(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 4.5
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case12(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 5.5
        self.assertEqual(removals(arr, n, k), 1)
