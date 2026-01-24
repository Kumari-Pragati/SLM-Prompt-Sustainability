import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_nums(5, 3, 10, 20), 20)
        self.assertEqual(sum_nums(2, 2, 2, 4), 4)

    def test_edge_and_boundary(self):
        self.assertEqual(sum_nums(0, 0, 0, 1), 0)
        self.assertEqual(sum_nums(100, 100, -1, 0), None)
        self.assertEqual(sum_nums(-10, -10, 0, 10), None)

    def test_complex(self):
        self.assertEqual(sum_nums(-5, 5, 0, 5), None)
        self.assertEqual(sum_nums(10, -10, -20, -10), None)
        self.assertEqual(sum_nums(float('inf'), float('inf'), float('-inf'), float('-inf')), None)
