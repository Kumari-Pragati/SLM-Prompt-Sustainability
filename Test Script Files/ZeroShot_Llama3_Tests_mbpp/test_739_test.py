import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_find_index(self):
        self.assertEqual(find_Index(1), 10)
        self.assertEqual(find_Index(2), 32)
        self.assertEqual(find_Index(3), 100)
        self.assertEqual(find_Index(4), 316)
        self.assertEqual(find_Index(5), 1000)
        self.assertEqual(find_Index(6), 3162)
        self.assertEqual(find_Index(7), 10000)
        self.assertEqual(find_Index(8), 31623)
        self.assertEqual(find_Index(9), 100000)
        self.assertEqual(find_Index(10), 316227)
        self.assertEqual(find_Index(11), 1000000)
        self.assertEqual(find_Index(12), 3162277)
        self.assertEqual(find_Index(13), 10000000)
        self.assertEqual(find_Index(14), 31622776)
        self.assertEqual(find_Index(15), 100000000)
        self.assertEqual(find_Index(16), 316227766)
        self.assertEqual(find_Index(17), 1000000000)
        self.assertEqual(find_Index(18), 316227766016)
        self.assertEqual(find_Index(19), 1000000000000)
        self.assertEqual(find_Index(20), 1000000000000000)

    def test_find_index_edge_cases(self):
        self.assertRaises(OverflowError, find_Index, 21)
