import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_single_element(self):
        self.assertEqual(move_first([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(move_first([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_large_list(self):
        self.assertEqual(move_first(list(range(1, 1001))), list(range(1000, 0, -1)) + [999])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            move_first(123)
        with self.assertRaises(TypeError):
            move_first('123')
        with self.assertRaises(TypeError):
            move_first(None)
