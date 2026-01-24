import unittest
from549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_num_sum_1(self):
        self.assertEqual(odd_Num_Sum(1), 1)

    def test_odd_num_sum_3(self):
        self.assertEqual(odd_Num_Sum(3), 343)

    def test_odd_num_sum_5(self):
        self.assertEqual(odd_Num_Sum(5), 343003)

    def test_odd_num_sum_101(self):
        self.assertEqual(odd_Num_Sum(101), 136273876601)
