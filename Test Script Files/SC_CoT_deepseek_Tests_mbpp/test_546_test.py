import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurrenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char("hello", "l"), 4)

    def test_edge_case_char_not_found(self):
        self.assertIsNone(last_occurence_char("hello", "z"))

    def test_edge_case_empty_string(self):
        self.assertIsNone(last_occurence_char("", "a"))

    def test_special_case_char_at_end(self):
        self.assertEqual(last_occurence_char("hello", "o"), 6)

    def test_invalid_input_none_string(self):
        with self.assertRaises(TypeError):
            last_occurence_char(None, "a")

    def test_invalid_input_none_char(self):
        with self.assertRaises(TypeError):
            last_occurence_char("hello", None)
