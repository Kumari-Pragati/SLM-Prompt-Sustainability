import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_column([[1, 2, 3], [4, 5, 6]], 1), 6)
        self.assertEqual(sum_column([[7, 8, 9], [10, 11, 12]], 2), 22)

    def test_edge_cases(self):
        self.assertEqual(sum_column([], 0), 0)
        self.assertEqual(sum_column([[0]], 0), 0)
        self.assertEqual(sum_column([[1]], 0), 0)
        self.assertEqual(sum_column([[1]], 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_column([[2**31], [2**31]], 0), 2**31)
        self.assertEqual(sum_column([[2**31-1], [2**31]], 0), 2**31-1)
        self.assertEqual(sum_column([[2**31], [2**31-1]], 1), 2**31)

    def test_negative_values(self):
        self.assertEqual(sum_column([[-1, -2, -3], [-4, -5, -6]], 1), -15)

    def test_mixed_types(self):
        self.assertRaises(TypeError, sum_column, [[1, 2, 3], [4, 5, "a"]], 1)
