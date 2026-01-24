import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_single_element_list(self):
        self.assertEqual(move_first([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(move_first([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_negative_numbers(self):
        self.assertEqual(move_first([-1, -2, -3]), [-3, -1, -2])

    def test_zero(self):
        self.assertEqual(move_first([0, 1, 2]), [2, 0, 1])

    def test_non_integer_elements(self):
        self.assertEqual(move_first(['a', 'b', 'c']), ['c', 'a', 'b'])

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            move_first([1, None, 2])
