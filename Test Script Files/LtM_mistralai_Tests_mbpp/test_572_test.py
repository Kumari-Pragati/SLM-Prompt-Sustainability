import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])
        self.assertListEqual(two_unique_nums([4, 4, 5, 6]), [5, 6])
        self.assertListEqual(two_unique_nums([1, 1, 1, 2, 2, 3]), [3])

    def test_edge_cases(self):
        self.assertListEqual(two_unique_nums([]), [])
        self.assertListEqual(two_unique_nums([1]), [1])
        self.assertListEqual(two_unique_nums([1, 1]), [])
        self.assertListEqual(two_unique_nums([1, 1, 1]), [])
        self.assertListEqual(two_unique_nums([2, 2, 2, 3, 3]), [3])

    def test_complex(self):
        self.assertListEqual(two_unique_nums([10, 20, 10, 30, 10, 40]), [20, 30, 40])
        self.assertListEqual(two_unique_nums([1, 1, 2, 2, 3, 4, 4, 5, 6]), [3, 5, 6])
