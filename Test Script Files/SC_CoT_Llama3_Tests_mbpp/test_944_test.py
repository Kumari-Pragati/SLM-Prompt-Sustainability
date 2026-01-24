import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(num_position("Hello123World"), 4)

    def test_edge_case_at_start(self):
        self.assertEqual(num_position("123HelloWorld"), 0)

    def test_edge_case_at_end(self):
        self.assertEqual(num_position("HelloWorld123"), 7)

    def test_multiple_numbers(self):
        self.assertEqual(num_position("Hello123World456"), 4)

    def test_no_numbers(self):
        self.assertIsNone(num_position("HelloWorld"))

    def test_single_digit(self):
        self.assertEqual(num_position("Hello1World"), 6)

    def test_multiple_digits(self):
        self.assertEqual(num_position("Hello123World"), 4)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            num_position(123)

    def test_invalid_input_empty(self):
        self.assertIsNone(num_position(""))
