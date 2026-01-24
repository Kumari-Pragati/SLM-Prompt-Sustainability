import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk"], 3), ["abc", "hijk"])

    def test_empty_string(self):
        self.assertEqual(extract_string([""], 0), [""])

    def test_all_same_length(self):
        self.assertEqual(extract_string(["abcd", "efgh", "ijkl"], 4), ["abcd", "efgh", "ijkl"])

    def test_no_match(self):
        self.assertEqual(extract_string(["abc", "defg", "hijk"], 2), [])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            extract_string(["abc", "defg", "hijk"], -1)

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            extract_string([123, "defg", "hijk"], 3)
