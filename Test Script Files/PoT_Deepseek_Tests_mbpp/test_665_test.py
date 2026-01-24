import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_last([1, 2, 3, 4, 1]), [1, 2, 3, 4, 1])

    def test_single_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_all_same_elements(self):
        self.assertEqual(move_last([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_all_different_elements(self):
        self.assertEqual(move_last([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_large_list(self):
        self.assertEqual(move_last(list(range(1, 1001))), list(range(1, 1001)))

    def test_duplicate_last_element(self):
        self.assertEqual(move_last([1, 2, 3, 4, 4]), [1, 2, 3, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(move_last([-1, -2, -3, -4]), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        self.assertEqual(move_last([-1, 0, 1, -2]), [-1, 0, 1, -2])
