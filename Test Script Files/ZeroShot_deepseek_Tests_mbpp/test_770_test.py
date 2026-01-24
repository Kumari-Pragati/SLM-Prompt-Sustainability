import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_Num_Sum(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 17)
        self.assertEqual(odd_Num_Sum(3), 193)
        self.assertEqual(odd_Num_Sum(4), 289)
        self.assertEqual(odd_Num_Sum(5), 625)
        self.assertEqual(odd_Num_Sum(6), 15625)
        self.assertEqual(odd_Num_Sum(7), 13841287201)
        self.assertEqual(odd_Num_Sum(8), 13841287201)
        self.assertEqual(odd_Num_Sum(9), 13841287201)
        self.assertEqual(odd_Num_Sum(10), 13841287201)
