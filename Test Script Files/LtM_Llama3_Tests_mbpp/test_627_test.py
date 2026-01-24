import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5],0,5),6)
        self.assertEqual(find_First_Missing([0,1,2,3,5,6],0,6),4)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,7],0,7),6)

    def test_edge(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6],0,6),7)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7],0,7),8)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8],0,8),9)

    def test_edge2(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9],0,9),10)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10],0,10),11)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11],0,11),12)

    def test_edge3(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12],0,12),13)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13],0,13),14)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],0,14),15)

    def test_edge4(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],0,15),16)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],0,16),17)
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],0,17),18)
