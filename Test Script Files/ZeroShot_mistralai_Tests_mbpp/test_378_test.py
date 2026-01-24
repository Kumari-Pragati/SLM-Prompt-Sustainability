import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_single_element_list(self):
        self.assertEqual(move_first([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])

    def test_list_with_duplicates(self):
        self.assertEqual(move_first([1, 1, 2, 3]), [3, 1, 1, 2])
