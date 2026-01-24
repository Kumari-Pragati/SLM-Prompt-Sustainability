import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_last([1, 2, 2, 3, 4, 2]), [1, 3, 4, 2, 2, 2])

    def test_single_element(self):
        self.assertEqual(move_last([5]), [5])

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_all_same_elements(self):
        self.assertEqual(move_last([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])

    def test_all_different_elements(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(move_last([-1, -2, -2, -3, -4]), [-1, -3, -4, -2, -2])

    def test_zero(self):
        self.assertEqual(move_last([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_large_numbers(self):
        self.assertEqual(move_last([1000, 2000, 3000, 2000]), [1000, 3000, 2000, 2000])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            move_last("1, 2, 2, 3, 4, 2")
