import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_find_kth(self):
        self.assertEqual(find_kth([1, 3, 5], [2, 4, 6], 3, 3, 3), 4)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 5), 5)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 10), 10)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 1), 1)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 2), 2)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 3), 3)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 4), 4)
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 5), 5)
