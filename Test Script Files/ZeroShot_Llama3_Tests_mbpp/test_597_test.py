import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_find_kth(self):
        self.assertEqual(find_kth([1, 3, 5, 7], [2, 4, 6, 8], 4, 4, 3), 5)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 4, 4, 4), 7)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 2, 4, 3), 6)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 4, 2, 3), 6)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 1, 4, 3), 7)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 4, 1, 3), 7)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 1, 1, 3), 7)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 4, 4, 1), 1)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 1, 4, 1), 1)
        self.assertEqual(find_kth([1, 2, 3, 4], [5, 6, 7, 8], 4, 1, 1), 1)
