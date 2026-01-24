import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_find_Extra(self):
        self.assertEqual(find_Extra([2, 4, 6, 8, 10], [2, 4, 6, 8], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(find_Extra([10, 20, 30, 40, 50], [10, 20, 30, 40], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6], 7), 6)
        self.assertEqual(find_Extra([], [], 0), 0)
