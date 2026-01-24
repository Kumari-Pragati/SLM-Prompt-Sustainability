import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_move_first_with_list(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])
        self.assertEqual(move_first(['a', 'b', 'c']), ['c', 'a', 'b'])

    def test_move_first_with_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_move_first_with_single_element_list(self):
        self.assertEqual(move_first([1]), [1])

    def test_move_first_with_duplicate_elements(self):
        self.assertEqual(move_first([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_move_first_with_none_elements(self):
        with self.assertRaises(TypeError):
            move_first([1, 2, None, 4])
