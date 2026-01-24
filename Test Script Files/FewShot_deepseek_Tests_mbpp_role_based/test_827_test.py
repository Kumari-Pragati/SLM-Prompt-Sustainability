import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 14)

    def test_edge_case(self):
        list1 = [[1], [2], [3]]
        C = 0
        self.assertEqual(sum_column(list1, C), 6)

    def test_boundary_case(self):
        list1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        C = 2
        self.assertEqual(sum_column(list1, C), 0)

    def test_invalid_input(self):
        list1 = "invalid_input"
        C = 1
        with self.assertRaises(TypeError):
            sum_column(list1, C)
