import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 9, 11, 15]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 14)

    def test_edge_case(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_boundary_case(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_special_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff("not an array", 5)
