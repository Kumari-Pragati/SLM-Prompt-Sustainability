import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_split_Arr(self):
        self.assertEqual(split_Arr([1,2,3,4,5], 5, 2), [3,4,5,1,2])
        self.assertEqual(split_Arr(['a', 'b', 'c', 'd', 'e'], 5, 3), ['d', 'e', 'a', 'b', 'c'])
        self.assertEqual(split_Arr([True, False, True, False, True], 5, 1), [False, True, True, False, True])
        self.assertEqual(split_Arr([], 0, 0), [])
        self.assertEqual(split_Arr([1,2,3,4,5], 5, 0), [1,2,3,4,5])
        self.assertEqual(split_Arr([1,2,3,4,5], 5, 5), [1,2,3,4,5])
