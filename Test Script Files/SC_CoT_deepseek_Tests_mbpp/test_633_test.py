import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairOrSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28)

    def test_edge_case(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_boundary_case(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 3)

    def test_special_case(self):
        arr = [1, 2, 2, 1]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            pair_OR_Sum("1, 2, 3, 4", 4)
