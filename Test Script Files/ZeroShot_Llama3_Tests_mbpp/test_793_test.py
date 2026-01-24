import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):

    def test_last(self):
        self.assertEqual(last([1,2,3,4,5], 3, 5), 2)
        self.assertEqual(last([5,4,3,2,1], 3, 5), 2)
        self.assertEqual(last([1,2,3,4,5], 0, 5), 0)
        self.assertEqual(last([1,2,3,4,5], 6, 5), -1)
        self.assertEqual(last([1,2,3,4,5], 5, 5), 4)
        self.assertEqual(last([1,2,3,4,5], 4, 5), 3)
        self.assertEqual(last([1,2,3,4,5], 3, 5), 2)
        self.assertEqual(last([1,2,3,4,5], 2, 5), 1)
        self.assertEqual(last([1,2,3,4,5], 1, 5), 0)
        self.assertEqual(last([1,2,3,4,5], 5, 5), 4)

    def test_last_edge_cases(self):
        self.assertEqual(last([], 3, 0), -1)
        self.assertEqual(last([1], 3, 1), -1)
        self.assertEqual(last([1], 1, 1), 0)
        self.assertEqual(last([1], 0, 1), -1)
