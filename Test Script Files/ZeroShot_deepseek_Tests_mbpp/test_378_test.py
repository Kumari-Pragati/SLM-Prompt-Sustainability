import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_move_first_with_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_move_first_with_single_element_list(self):
        self.assertEqual(move_first([1]), [1])

    def test_move_first_with_multiple_elements_list(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])

    def test_move_first_with_duplicate_elements_list(self):
        self.assertEqual(move_first([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_move_first_with_negative_elements_list(self):
        self.assertEqual(move_first([-1, -2, -3]), [-3, -1, -2])

    def test_move_first_with_mixed_elements_list(self):
        self.assertEqual(move_first([1, -2, 3, -4]), [-4, 1, -2, 3])
