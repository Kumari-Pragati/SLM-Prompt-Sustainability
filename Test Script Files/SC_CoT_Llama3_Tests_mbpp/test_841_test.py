import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_typical_input(self):
        arr = [5, 2, 8, 6, 1, 3]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 4)

    def test_edge_case(self):
        arr = [1, 2, 3]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case2(self):
        arr = [5, 5, 5]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case3(self):
        arr = []
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case4(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case5(self):
        arr = [1, 1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case6(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case7(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case8(self):
        arr = [5, 4, 3, 2, 1, 0]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case9(self):
        arr = [5, 4, 3, 2, 1, 0, -1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case10(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case11(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case12(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case13(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case14(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_edge_case15(self):
        arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)
