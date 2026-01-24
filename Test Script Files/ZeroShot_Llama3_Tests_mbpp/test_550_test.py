import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 1, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 1, 4), 4)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 2, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 2, 4), 3)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 3, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 3, 4), 2)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 4, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 4, 4), 1)

    def test_find_max_edge_cases(self):
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([5], 0, 0), 5)
        self.assertEqual(find_Max([1, 2], 0, 1), 2)
        self.assertEqual(find_Max([2, 1], 0, 1), 2)
        self.assertEqual(find_Max([1, 2, 3], 0, 2), 3)
        self.assertEqual(find_Max([3, 2, 1], 0, 2), 3)
