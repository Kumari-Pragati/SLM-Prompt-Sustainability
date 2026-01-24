import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_find_closet(self):
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 3, 4, 4), (1, 5, 9))
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 4, 3, 4), (2, 6, 10))
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 4, 4, 3), (3, 7, 11))
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 3, 4, 5), (4, 8, 12))
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 5, 4, 3), (1, 5, 9))
