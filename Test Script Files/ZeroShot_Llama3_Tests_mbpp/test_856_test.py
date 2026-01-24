import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_find_Min_Swaps(self):
        self.assertEqual(find_Min_Swaps([0,1,0,1], 4), 2)
        self.assertEqual(find_Min_Swaps([1,1,0,0], 4), 0)
        self.assertEqual(find_Min_Swaps([0,0,1,1], 4), 2)
        self.assertEqual(find_Min_Swaps([1,0,1,0], 4), 2)
        self.assertEqual(find_Min_Swaps([0,0,0,0], 4), 4)
        self.assertEqual(find_Min_Swaps([1,1,1,1], 4), 0)
        self.assertEqual(find_Min_Swaps([0,1,1,0], 4, 2)
        self.assertEqual(find_Min_Swaps([1,0,0,1], 4), 2)
        self.assertEqual(find_Min_Swaps([0,1,0,1], 4), 2)
        self.assertEqual(find_Min_Swaps([1,1,0,0], 4), 0)
        self.assertEqual(find_Min_Swaps([0,0,1,1], 4), 2)
        self.assertEqual(find_Min_Swaps([1,0,1,0], 4), 2)
        self.assertEqual(find_Min_Swaps([0,0,0,0], 4), 4)
        self.assertEqual(find_Min_Swaps([1,1,1,1], 4), 0)
