import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(3), 33)
        self.assertEqual(odd_Num_Sum(5), 3375)

    def test_edge_and_boundary(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(1000000), 10725929545400000000)
        self.assertEqual(odd_Num_Sum(17), 1568039453183)

    def test_complex(self):
        self.assertEqual(odd_Num_Sum(2147483647), 18446744073709551615)
        self.assertEqual(odd_Num_Sum(2147483646), 18446744073709551615)
        self.assertEqual(odd_Num_Sum(2147483648), 0)
