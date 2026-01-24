import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])

    def test_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_single_element_list(self):
        self.assertEqual(move_first([4]), [4])

    def test_duplicate_elements_list(self):
        self.assertEqual(move_first([5, 5, 5]), [5, 5, 5])

    def test_large_list(self):
        self.assertEqual(move_first(list(range(1, 101))), list(range(100, 0, -1)) + [99])
