import unittest
from mbpp_225_code import find_Min

class TestFind_Min(unittest.TestCase):

    def test_find_Min(self):
        self.assertEqual(find_Min([1,2,3,4,5],0,4), 5)
        self.assertEqual(find_Min([5,4,3,2,1],0,4), 1)
        self.assertEqual(find_Min([5,5,5,5,5],0,4), 5)
        self.assertEqual(find_Min([1,2,3,4,5,5],0,5), 5)
        self.assertEqual(find_Min([1,2,3,4,5,6],0,5), 5)
        self.assertEqual(find_Min([1,2,3,4,5,6,7],0,6), 7)
        self.assertEqual(find_Min([1,2,3,4,5,6,7,8],0,7), 8)
        self.assertEqual(find_Min([1,2,3,4,5,6,7,8,9],0,8), 9)
        self.assertEqual(find_Min([1,2,3,4,5,6,7,8,9,10],0,9), 10)

    def test_find_Min_edge_cases(self):
        self.assertEqual(find_Min([1],0,0), 1)
        self.assertEqual(find_Min([1,2],0,1), 2)
        self.assertEqual(find_Min([1,2,3],0,2), 3)
        self.assertEqual(find_Min([1,2,3,4],0,3), 4)
        self.assertEqual(find_Min([1,2,3,4,5],0,4), 5)
