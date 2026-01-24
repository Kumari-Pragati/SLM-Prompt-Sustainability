import unittest
from mbpp_109_code import odd_Equivalent

class TestOddEquivalent(unittest.TestCase):

    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent('1011', 4), 3)
        self.assertEqual(odd_Equivalent('11001', 5), 2)
        self.assertEqual(odd_Equivalent('11111', 5), 5)
        self.assertEqual(odd_Equivalent('00000', 5), 0)
        self.assertEqual(odd_Equivalent('111000111', 7), 4)
