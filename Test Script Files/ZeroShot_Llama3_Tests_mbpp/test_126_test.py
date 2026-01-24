import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_sum_function(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(2, 3), 1)
        self.assertEqual(sum(4, 6), 2)
        self.assertEqual(sum(5, 5), 0)
        self.assertEqual(sum(10, 15), 3)
        self.assertEqual(sum(20, 25), 4)
        self.assertEqual(sum(30, 30), 0)
        self.assertEqual(sum(40, 50), 4)
        self.assertEqual(sum(60, 90), 6)
        self.assertEqual(sum(100, 200), 10)
        self.assertEqual(sum(1000, 2000), 10)

    def test_sum_function_edge_cases(self):
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-2, 2), 0)
        self.assertEqual(sum(-5, 5), 0)
        self.assertEqual(sum(-10, 10), 0)
        self.assertEqual(sum(-20, 20), 0)
        self.assertEqual(sum(-30, 30), 0)
        self.assertEqual(sum(-40, 40), 0)
        self.assertEqual(sum(-50, 50), 0)
        self.assertEqual(sum(-60, 60), 0)
        self.assertEqual(sum(-100, 100), 0)
        self.assertEqual(sum(-1000, 1000), 0)
