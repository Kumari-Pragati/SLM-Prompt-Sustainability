import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 5), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(left_insertion([2], 1), 0)
        self.assertEqual(left_insertion([2], 3), 1)

    def test_edge_case_insert_smaller_than_all(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 0), 0)

    def test_edge_case_insert_larger_than_all(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 10), 4)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            left_insertion(123, 5)

    def test_invalid_input_non_comparable(self):
        with self.assertRaises(TypeError):
            left_insertion(['a', 'b', 'c'], 5)
