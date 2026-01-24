import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_num('Hello123World'), 'Hello123World')

    def test_edge_case_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_edge_case_single_digit(self):
        self.assertEqual(move_num('a1b'), 'a1b')

    def test_edge_case_single_non_digit(self):
        self.assertEqual(move_num('a'), 'a')

    def test_edge_case_multiple_digits(self):
        self.assertEqual(move_num('abc123def456'), 'abc123def456')

    def test_edge_case_multiple_non_digits(self):
        self.assertEqual(move_num('abcdef'), 'abcdef')

    def test_edge_case_mixed_digits_non_digits(self):
        self.assertEqual(move_num('a1b2c3d4e5f6'), 'a1b2c3d4e5f6')

    def test_edge_case_mixed_digits_non_digits_reversed(self):
        self.assertEqual(move_num('f6e5d4c3b2a1'), 'f6e5d4c3b2a1')

    def test_edge_case_mixed_digits_non_digits_empty(self):
        self.assertEqual(move_num('a1b2c3d4e5f6' +'' + 'abcdef'), 'a1b2c3d4e5f6abcdef')

    def test_edge_case_mixed_digits_non_digits_empty_reversed(self):
        self.assertEqual(move_num('f6e5d4c3b2a1' +'' + 'abcdef'), 'f6e5d4c3b2a1abcdef')
