import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_list('A1B2C3D4'), ['A1', 'B2', 'C3', 'D4'])

    def test_edge_case_single_letter(self):
        self.assertEqual(split_list('A'), ['A'])

    def test_edge_case_no_letters(self):
        self.assertEqual(split_list('12345'), [])

    def test_boundary_case_empty_string(self):
        self.assertEqual(split_list(''), [])

    def test_corner_case_multiple_consecutive_letters(self):
        self.assertEqual(split_list('ABCD'), ['ABCD'])

    def test_corner_case_multiple_consecutive_numbers(self):
        self.assertEqual(split_list('1234'), ['1234'])

    def test_corner_case_mixed_letters_and_numbers(self):
        self.assertEqual(split_list('A1B2C3'), ['A1', 'B2', 'C3'])
