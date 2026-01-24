import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(num_position("123abc"), 0)

    def test_edge_condition_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_edge_condition_no_numbers(self):
        self.assertIsNone(num_position("abc"))

    def test_boundary_condition_single_number(self):
        self.assertEqual(num_position("1"), 0)

    def test_boundary_condition_multiple_numbers(self):
        self.assertEqual(num_position("12345"), 0)

    def test_complex_case_numbers_at_end(self):
        self.assertEqual(num_position("abc123"), 3)

    def test_complex_case_numbers_in_middle(self):
        self.assertEqual(num_position("abc1def"), 3)
