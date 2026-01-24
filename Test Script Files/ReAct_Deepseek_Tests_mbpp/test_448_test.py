import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 9)
        self.assertEqual(cal_sum(4), 15)

    def test_edge_cases(self):
        self.assertEqual(cal_sum(-1), 5)
        self.assertEqual(cal_sum(-10), 5)
        self.assertEqual(cal_sum(5), 25)
        self.assertEqual(cal_sum(10), 141)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(cal_sum('a'), 5)
        self.assertEqual(cal_sum([1,2,3]), 25)
        self.assertEqual(cal_sum({'a':1, 'b':2}), 25)
