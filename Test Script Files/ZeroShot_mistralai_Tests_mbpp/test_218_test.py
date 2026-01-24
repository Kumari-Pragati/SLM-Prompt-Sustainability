import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):

    def test_min_operations(self):
        self.assertEqual(min_Operations(2, 4), 1)
        self.assertEqual(min_Operations(5, 9), 2)
        self.assertEqual(min_Operations(10, 15), 4)
        self.assertEqual(min_Operations(12, 8), 1)
        self.assertEqual(min_Operations(20, 24), 3)
        self.assertEqual(min_Operations(44, 64), 6)
        self.assertEqual(min_Operations(17, 23), 4)
        self.assertEqual(min_Operations(38, 50), 7)
        self.assertEqual(min_Operations(77, 98), 11)
        self.assertEqual(min_Operations(100, 169), 15)
