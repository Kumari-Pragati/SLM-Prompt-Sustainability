import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_single_element(self):
        self.assertEqual(move_first([1]), [1])

    def test_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_negative_numbers(self):
        self.assertEqual(move_first([-1, -2, -3]), [-3, -1, -2])

    def test_duplicate_elements(self):
        self.assertEqual(move_first([1, 2, 2, 3]), [3, 1, 2, 2])

    def test_large_numbers(self):
        self.assertEqual(move_first([100, 200, 300]), [300, 100, 200])

    def test_non_integer_elements(self):
        self.assertEqual(move_first(['a', 'b', 'c']), ['c', 'a', 'b'])

    def test_mixed_types(self):
        self.assertEqual(move_first([1, 'a', 2.5]), [2.5, 1, 'a'])
