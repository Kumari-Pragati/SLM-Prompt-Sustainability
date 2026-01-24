import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_single_element_list(self):
        self.assertEqual(move_last([1]), [])
        self.assertEqual(move_last([2]), [2])

    def test_multiple_elements_list(self):
        self.assertEqual(move_last([1, 1, 2]), [2, 1])
        self.assertEqual(move_last([2, 1, 1]), [2, 1, 1])
        self.assertEqual(move_last([1, 2, 1]), [2, 1])

    def test_duplicate_elements_at_beginning(self):
        self.assertEqual(move_last([1, 1, 1, 2]), [2, 1, 1])
        self.assertEqual(move_last([2, 2, 1]), [2, 1, 2])

    def test_duplicate_elements_in_middle(self):
        self.assertEqual(move_last([1, 1, 2, 1, 1]), [2, 1, 1, 1])
        self.assertEqual(move_last([2, 1, 2, 1]), [2, 1, 2, 1])

    def test_duplicate_elements_at_end(self):
        self.assertEqual(move_last([1, 1, 1]), [1, 1])
        self.assertEqual(move_last([2, 2]), [2, 2])

    def test_invalid_input_non_list(self):
        self.assertRaises(TypeError, move_last, "string")
