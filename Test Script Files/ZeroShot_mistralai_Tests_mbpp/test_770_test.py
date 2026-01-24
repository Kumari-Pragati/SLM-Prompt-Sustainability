import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_num_sum_1(self):
        self.assertEqual(odd_Num_Sum(1), 1)

    def test_odd_num_sum_3(self):
        self.assertEqual(odd_Num_Sum(3), 34)

    def test_odd_num_sum_5(self):
        self.assertEqual(odd_Num_Sum(5), 225)

    def test_odd_num_sum_7(self):
        self.assertEqual(odd_Num_Sum(7), 1138)

    def test_odd_num_sum_9(self):
        self.assertEqual(odd_Num_Sum(9), 5913)

    def test_odd_num_sum_11(self):
        self.assertEqual(odd_Num_Sum(11), 33075)
