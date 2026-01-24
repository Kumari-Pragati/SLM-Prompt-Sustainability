import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_move_first(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])
        self.assertEqual(move_first([10, 20, 30, 40, 50]), [50, 10, 20, 30, 40])
        self.assertEqual(move_first(['a', 'b', 'c', 'd', 'e']), ['e', 'a', 'b', 'c', 'd'])
        self.assertEqual(move_first([1, 2, 3, 4]), [4, 1, 2, 3])
        self.assertEqual(move_first(['apple', 'banana', 'cherry', 'date']), ['date', 'apple', 'banana', 'cherry'])

    def test_move_first_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_move_first_single_element_list(self):
        self.assertEqual(move_first([1]), [1])
