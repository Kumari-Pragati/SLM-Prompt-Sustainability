import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 1, 4), [[1, 2], [3, 4]])

    def test_edge_case_leftrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 2, 4), [[3, 4]])

    def test_edge_case_rightrange(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 1, 3), [[1, 2]])

    def test_edge_case_both_ranges(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 2, 3), [])

    def test_special_case_single_element(self):
        self.assertEqual(remove_list_range([[2]], 1, 3), [])

    def test_special_case_empty_list(self):
        self.assertEqual(remove_list_range([], 1, 3), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            remove_list_range(123, 1, 3)

    def test_invalid_input_non_integer_in_list(self):
        with self.assertRaises(TypeError):
            remove_list_range([[1, '2'], [3, 4]], 1, 4)
