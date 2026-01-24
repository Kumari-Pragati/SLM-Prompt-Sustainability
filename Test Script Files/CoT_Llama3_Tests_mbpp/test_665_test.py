import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_move_last_typical(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_move_last_edge(self):
        self.assertEqual(move_last([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_move_last_edge2(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5, 5]), [2, 3, 4, 5, 5, 1])

    def test_move_last_invalid(self):
        with self.assertRaises(TypeError):
            move_last("abc")

    def test_move_last_empty(self):
        self.assertEqual(move_last([]), [])

    def test_move_last_single(self):
        self.assertEqual(move_last([1]), [1])

    def test_move_last_single2(self):
        self.assertEqual(move_last([1, 1]), [1, 1])
