import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_remove_tuple(self):
        self.assertEqual(remove_tuple((1, 2, 3, 2, 4)), (1, 2, 3, 4))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_tuple((1, 2, 2, 3, 3, 4)), (1, 2, 3, 4))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3, 3, 4, 4)), (1, 2, 3, 4))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8)), (1, 2, 3, 4, 5, 6, 7, 8))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9)), (1, 2, 3, 4, 5, 6, 7, 8, 9))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
        self.assertEqual(remove_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
        self.assertEqual(remove_tuple((1, 2, 3,