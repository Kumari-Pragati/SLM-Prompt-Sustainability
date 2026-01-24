import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 9)
        self.assertEqual(cal_sum(4), 17)

    def test_edge_cases(self):
        self.assertEqual(cal_sum(-1), 3)  # Negative input should be handled as 0
        self.assertEqual(cal_sum(5), 53)  # Larger input should still work

    def test_boundary_cases(self):
        self.assertEqual(cal_sum(10), 1047)  # Larger boundary case
