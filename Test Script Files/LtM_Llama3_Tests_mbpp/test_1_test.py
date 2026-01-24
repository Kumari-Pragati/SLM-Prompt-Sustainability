import unittest
from mbpp_1_code import min_cost

class TestMinCost(unittest.TestCase):
    def test_simple(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_cost(cost, 3, 3), 28)

    def test_edge1(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_cost(cost, 2, 3), 11)

    def test_edge2(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(min_cost(cost, 4, 3), 28)

    def test_edge3(self):
        cost = [[1, 2, 3]]
        self.assertEqual(min_cost(cost, 1, 3), 6)

    def test_edge4(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        self.assertEqual(min_cost(cost, 5, 3), 28)

    def test_invalid_input1(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            min_cost(cost, 0, 3)

    def test_invalid_input2(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            min_cost(cost, 2, 0)

    def test_invalid_input3(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            min_cost(cost, 2, 4)
