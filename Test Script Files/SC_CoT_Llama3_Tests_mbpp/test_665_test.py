import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(move_last([1, 2, 3, 1, 2, 3]), [2, 3, 1, 2, 3, 1])

    def test_edge_case_single_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_edge_case_single_element_list(self):
        self.assertEqual(move_last([1, 1, 1]), [1, 1, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(move_last([1, 2, 2, 3, 3, 3]), [2, 2, 3, 3, 3, 1])

    def test_edge_case_list_with_duplicates_and_single_element(self):
        self.assertEqual(move_last([1, 2, 2, 3, 3, 3, 1]), [2, 2, 3, 3, 3, 1, 1])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            move_last('abc')

    def test_invalid_input_empty_string(self):
        with self.assertRaises(TypeError):
            move_last('')

    def test_invalid_input_list_with_non_integers(self):
        with self.assertRaises(TypeError):
            move_last(['a', 1, 2, 3])
