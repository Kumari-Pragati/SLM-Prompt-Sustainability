import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3, 4, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3, 3)), (1, 2, 3))

    def test_edge_case_empty_input(self):
        self.assertEqual(remove_tuple(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_edge_case_single_element_duplicates(self):
        self.assertEqual(remove_tuple((1, 1)), (1,))

    def test_edge_case_all_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 1, 1)), (1,))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            remove_tuple(123)

    def test_invalid_input_non_hashable(self):
        with self.assertRaises(TypeError):
            remove_tuple([1, 2, 3])
