import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(sum(12, 24), 12)
        self.assertEqual(sum(24, 12), 12)
        self.assertEqual(sum(28, 28), 28)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(1, 0), 0)
        self.assertEqual(sum(1, -1), 0)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), 0)
        self.assertEqual(sum(1, 2**31), 0)
        self.assertEqual(sum(2**31, 1), 0)

    def test_special_cases(self):
        self.assertEqual(sum(4, 2), 2)
        self.assertEqual(sum(6, 4), 2)
        self.assertEqual(sum(8, 6), 2)
        self.assertEqual(sum(10, 8), 2)
        self.assertEqual(sum(12, 10), 2)
        self.assertEqual(sum(14, 12), 2)
        self.assertEqual(sum(16, 14), 2)
        self.assertEqual(sum(18, 16), 2)
        self.assertEqual(sum(20, 18), 2)
        self.assertEqual(sum(22, 20), 2)
        self.assertEqual(sum(24, 22), 2)
        self.assertEqual(sum(26, 24), 2)
        self.assertEqual(sum(28, 26), 2)
