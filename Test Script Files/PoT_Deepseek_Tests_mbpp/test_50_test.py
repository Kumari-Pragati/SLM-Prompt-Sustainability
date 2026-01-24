import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length_list(['abc', 'de', 'fghi']), (2, 'de'))

    def test_edge_case_empty_list(self):
        self.assertEqual(min_length_list([]), (0, ''))

    def test_boundary_case_single_element(self):
        self.assertEqual(min_length_list(['abc']), (3, 'abc'))

    def test_corner_case_all_same_length(self):
        self.assertEqual(min_length_list(['abcd', 'efgh', 'ijkl']), (4, 'abcd'))

    def test_corner_case_empty_strings(self):
        self.assertEqual(min_length_list(['', '']), (0, ''))

    def test_corner_case_mixed_types(self):
        with self.assertRaises(TypeError):
            min_length_list(['abc', 123, None])
