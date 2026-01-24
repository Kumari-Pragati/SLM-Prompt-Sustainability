import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])
        self.assertEqual(move_first(['a', 'b', 'c']), ['c', 'a', 'b'])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(move_first([1]), [1])
        self.assertEqual(move_first([]), [])
        self.assertEqual(move_first([1, 2]), [2, 1])
        self.assertEqual(move_first(['a']), ['a'])

    def test_mixed_types(self):
        self.assertEqual(move_first([1, 'a', 2]), ['a', 1, 2])
        self.assertEqual(move_first(['a', 1, 'b']), ['b', 'a', 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            move_first(123)
