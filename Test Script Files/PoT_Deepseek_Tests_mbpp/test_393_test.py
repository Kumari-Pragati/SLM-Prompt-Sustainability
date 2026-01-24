import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length_list(['abc', 'defgh', 'ijklm']), (5, 'defgh'))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_length_list([]), (0, ''))

    def test_boundary_case_single_element(self):
        self.assertEqual(max_length_list(['abc']), (3, 'abc'))

    def test_corner_case_all_same_length(self):
        self.assertEqual(max_length_list(['abcd', 'efgh', 'ijkl']), (4, 'abcd'))

    def test_corner_case_all_different_lengths(self):
        self.assertEqual(max_length_list(['a', 'ab', 'abc']), (3, 'abc'))
