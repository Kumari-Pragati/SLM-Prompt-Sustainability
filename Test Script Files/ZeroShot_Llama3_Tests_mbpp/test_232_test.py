import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_larg_nnum(self):
        self.assertEqual(larg_nnum([1,2,3,4,5],2), [5,4])
        self.assertEqual(larg_nnum([-1,-2,-3,-4,-5],3), [-1,-2,-3])
        self.assertEqual(larg_nnum([10,20,30,40,50],1), [50])
        self.assertEqual(larg_nnum([1,2,3,4,5,6,7,8,9,10],5), [10,9,8,7,6])
        self.assertEqual(larg_nnum([-10,-20,-30,-40,-50],3), [-10,-20,-30])

    def test_larg_nnum_edge_cases(self):
        self.assertEqual(larg_nnum([],0), [])
        self.assertEqual(larg_nnum([1],1), [1])
        self.assertEqual(larg_nnum([1,2],1), [2])
        self.assertEqual(larg_nnum([1,2,3,4,5],0), [])
