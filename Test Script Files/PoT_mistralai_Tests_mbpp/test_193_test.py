import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_tuple((1, 2, 3, 2, 1)), (1, 2, 3))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(remove_tuple(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3)), (1, 2, 3))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(remove_tuple((-1, 0, 1)), (-1, 0, 1))

    def test_corner_case_floats(self):
        self.assertEqual(remove_tuple((1.0, 2.0, 3.0)), (1.0, 2.0, 3.0))

    def test_corner_case_mixed_types(self):
        self.assertEqual(remove_tuple((1, 'a', 2)), (1, 'a'))
