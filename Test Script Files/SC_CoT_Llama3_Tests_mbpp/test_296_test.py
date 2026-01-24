import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case2(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case4(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case6(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case7(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case8(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case9(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case10(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case11(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case12(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case13(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case14(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case15(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case16(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case17(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case18(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case19(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 4)

    def test_edge_case20(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_Inv_Count(arr, n), 0)

    def test_edge_case21(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_Inv