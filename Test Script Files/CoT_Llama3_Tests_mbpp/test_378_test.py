import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_first([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_first([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(move_first([1]), [1])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(move_first([1, 2, 2, 3, 1]), [1, 3, 2, 2, 1])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            move_first("test")

    def test_invalid_input_list_with_non_int_elements(self):
        with self.assertRaises(TypeError):
            move_first([1, "test", 3, 4, 5])
