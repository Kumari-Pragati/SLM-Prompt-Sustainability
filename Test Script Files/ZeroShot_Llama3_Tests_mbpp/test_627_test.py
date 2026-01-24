import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9],0,9), 10)
        self.assertEqual(find_First_Missing([0,1,2,3,5,6,7,8,9],0,9), 4)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,10],0,10), 9)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,11],0,11), 10)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10],0,10), 11)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12],0,12), 13)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13],0,13), 14)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],0,14), 15)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],0,15), 16)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],0,16), 17)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],0,17), 18)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],0,18), 19)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],0,19), 20)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],0,20), 21)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],0,21), 22)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],0,22), 23)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],0,23), 24)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],0,24), 25)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],0,25), 26)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25