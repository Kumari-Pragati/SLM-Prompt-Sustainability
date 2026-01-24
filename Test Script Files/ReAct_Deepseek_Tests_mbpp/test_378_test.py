import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_move_first_typical_case(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_move_first_single_element(self):
        self.assertEqual(move_first([1]), [1])

    def test_move_first_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_move_first_negative_numbers(self):
        self.assertEqual(move_first([-1, -2, -3, -4, -5]), [-5, -1, -2, -3, -4])

    def test_move_first_duplicates(self):
        self.assertEqual(move_first([1, 2, 2, 3, 4]), [4, 1, 2, 2, 3])

    def test_move_first_non_integer_elements(self):
        self.assertEqual(move_first(['a', 'b', 'c', 'd', 'e']), ['e', 'a', 'b', 'c', 'd'])

    def test_move_first_mixed_types(self):
        self.assertEqual(move_first([1, 'a', 3.0, 'b', 5]), [5, 1, 'a', 3.0, 'b'])
