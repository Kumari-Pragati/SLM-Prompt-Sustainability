import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):

    def test_simple_sum(self):
        self.assertEqual(sum_nums(1, 2, 0, 5), 20)
        self.assertEqual(sum_nums(3, 4, 7, 10), 20)
        self.assertEqual(sum_nums(0, 0, -10, 10), 20)

    def test_boundary_conditions(self):
        self.assertEqual(sum_nums(0, 0, 0, 10), 0)
        self.assertEqual(sum_nums(10, -10, -20, 0), -10)
        self.assertEqual(sum_nums(1000, 2000, 3000, 4000), 3000)

    def test_edge_cases(self):
        self.assertEqual(sum_nums(1000, 2000, 2000, 3000), 2000)
        self.assertEqual(sum_nums(-1000, -2000, -3000, -2000), -2000)
        self.assertEqual(sum_nums(0, 0, -1, 1), 0)
