import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(move_last([1, 2, 3]), [2, 3, 1, 1])
        self.assertEqual(move_last([1, 1, 2, 3]), [2, 3, 1, 1])
        self.assertEqual(move_last([1, 1, 1, 2, 3]), [2, 3, 1, 1, 1])

    def test_edge(self):
        self.assertEqual(move_last([]), [])
        self.assertEqual(move_last([1]), [1])
        self.assertEqual(move_last([1, 1]), [1, 1])

    def test_edge2(self):
        self.assertEqual(move_last([1, 2, 3, 1, 2, 3]), [2, 3, 1, 2, 3, 1])
        self.assertEqual(move_last([1, 1, 1, 2, 2, 2, 3, 3, 3]), [2, 2, 2, 3, 3, 3, 1, 1, 1])

    def test_edge3(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])
        self.assertEqual(move_last([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 1, 1, 1])
