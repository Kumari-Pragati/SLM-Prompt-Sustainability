import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(num_position("Hello123World"), 4)

    def test_edge_case_start(self):
        self.assertEqual(num_position("123HelloWorld"), 0)

    def test_edge_case_end(self):
        self.assertEqual(num_position("HelloWorld456"), 11)

    def test_multiple_numbers(self):
        self.assertEqual(num_position("Hello123World456"), 4)

    def test_no_numbers(self):
        self.assertIsNone(num_position("HelloWorld"))

    def test_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_single_number(self):
        self.assertEqual(num_position("123HelloWorld"), 0)

    def test_multiple_numbers_at_start(self):
        self.assertEqual(num_position("123456HelloWorld"), 0)

    def test_multiple_numbers_at_end(self):
        self.assertEqual(num_position("HelloWorld123456"), 11)
