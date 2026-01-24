import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_num('hello123world'), 'helloworld123')

    def test_edge_case_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_edge_case_single_digit(self):
        self.assertEqual(move_num('1'), '1')

    def test_edge_case_single_non_digit(self):
        self.assertEqual(move_num('a'), 'a')

    def test_edge_case_single_digit_and_non_digit(self):
        self.assertEqual(move_num('a1'), 'a1')

    def test_edge_case_multiple_digits(self):
        self.assertEqual(move_num('123'), '123')

    def test_edge_case_multiple_non_digits(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_edge_case_multiple_digits_and_non_digits(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_edge_case_non_digit_at_start(self):
        self.assertEqual(move_num('a123'), 'a123')

    def test_edge_case_non_digit_at_end(self):
        self.assertEqual(move_num('123b'), '123b')

    def test_edge_case_non_digit_in_middle(self):
        self.assertEqual(move_num('12ab3'), '12ab3')

    def test_edge_case_non_digit_at_start_and_end(self):
        self.assertEqual(move_num('a123b'), 'a123b')

    def test_edge_case_non_digit_in_middle_and_end(self):
        self.assertEqual(move_num('12ab3c'), '12ab3c')
