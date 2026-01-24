import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_Num_Sum(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 17)
        self.assertEqual(odd_Num_Sum(3), 193)
        self.assertEqual(odd_Num_Sum(4), 1305)
        self.assertEqual(odd_Num_Sum(5), 6433)
