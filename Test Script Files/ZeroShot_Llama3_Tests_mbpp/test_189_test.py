import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_first_Missing_Positive(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5],5),1)
        self.assertEqual(first_Missing_Positive([1,2,0,4],4),3)
        self.assertEqual(first_Missing_Positive([1,3,6,4,2],5),5)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10],10),11)
        self.assertEqual(first_Missing_Positive([-1,2,3,4,5],5),1)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],15),16)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],16,17),17)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],20),21)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],25),26)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],30),31)
