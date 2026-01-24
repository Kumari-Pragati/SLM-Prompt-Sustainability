import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):

    def test_merge(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])
        self.assertEqual(merge([[1, 2, 3], [4, 5]]), [[1, 4], [2, 5], [3]])
        self.assertEqual(merge([[1], [2], [3]]), [[1, 2, 3]])
        self.assertEqual(merge([[], [], []]), [[]])
