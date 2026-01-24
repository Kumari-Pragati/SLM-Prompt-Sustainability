import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(move_last([1, 1, 2]), [2, 1])
        self.assertEqual(move_last([3, 3, 3]), [3])
        self.assertEqual(move_last([4, 4, 4, 5]), [5, 4, 4])

    def test_edge_cases(self):
        self.assertEqual(move_last([1]), [])
        self.assertEqual(move_last([1, 1]), [])
        self.assertEqual(move_last([1, 1, 1]), [])
        self.assertEqual(move_last([1, 1, 1, 2]), [2, 1, 1])
        self.assertEqual(move_last([2, 1, 1]), [1, 2])
        self.assertEqual(move_last([2, 1]), [1, 2])
        self.assertEqual(move_last([2]), [])

    def test_complex(self):
        self.assertEqual(move_last([1, 1, 2, 1, 1]), [1, 2, 1])
        self.assertEqual(move_last([1, 2, 1, 2, 1]), [2, 1, 2])
        self.assertEqual(move_last([1, 2, 1, 2, 3]), [3, 2, 1, 2])
        self.assertEqual(move_last([1, 2, 1, 2, 3, 1]), [3, 2, 1, 2, 1])
