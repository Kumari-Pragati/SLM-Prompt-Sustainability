import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent('111', 3), 3)
        self.assertEqual(odd_Equivalent('101', 3), 1)
        self.assertEqual(odd_Equivalent('110', 3), 1)
        self.assertEqual(odd_Equivalent('100', 3), 0)
        self.assertEqual(odd_Equivalent('111111', 6), 6)
        self.assertEqual(odd_Equivalent('101010', 6), 3)
        self.assertEqual(odd_Equivalent('110011', 6), 3)
        self.assertEqual(odd_Equivalent('100000', 6), 0)

    def test_edge_cases(self):
        self.assertEqual(odd_Equivalent('', 0), 0)
        self.assertEqual(odd_Equivalent('1', 1), 1)
        self.assertEqual(odd_Equivalent('0', 1), 0)
