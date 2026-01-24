import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a typical case"
        expected_output = "Thisisatypeofcase"
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_with_multiple_spaces(self):
        text = "This   is   a   case with   multiple   spaces"
        expected_output = "Thisisacasewithmultiplespaces"
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_with_tabs(self):
        text = "This\tis\ta\tcase\twith\ttabs"
        expected_output = "Thisisatacasewithtabs"
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_with_newlines(self):
        text = "This\nis\na\ncase\nwith\nnewlines"
        expected_output = "Thisisacasewithnewlines"
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_with_mixed_whitespaces(self):
        text = "This \t is \n a \t case \n with \t mixed \t whitespaces"
        expected_output = "Thisisatacasewithmixedwhitespaces"
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_empty_string(self):
        text = ""
        expected_output = ""
        self.assertEqual(remove_whitespaces(text), expected_output)

    def test_edge_case_single_whitespace(self):
        text = " "
        expected_output = ""
        self.assertEqual(remove_whitespaces(text), expected_output)
