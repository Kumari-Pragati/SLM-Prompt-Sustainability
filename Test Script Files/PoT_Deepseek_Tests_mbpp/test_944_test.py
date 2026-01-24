import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_position("123abc456"), 0)

    def test_edge_case_no_number(self):
        self.assertIsNone(num_position("abc"))

    def test_boundary_case_single_number(self):
        self.assertEqual(num_position("1"), 0)

    def test_corner_case_multiple_numbers(self):
        self.assertEqual(num_position("abc123def456"), 3)

    def test_invalid_input_empty_string(self):
        self.assertIsNone(num_position(""))
