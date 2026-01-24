import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")
        self.assertEqual(remove_Occ("Python", "n"), "Pytho")
        self.assertEqual(remove_Occ("12345", "5"), "1234")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_Occ("a", "a"), "")
        self.assertEqual(remove_Occ("", "a"), "")

    def test_edge_case_empty_char(self):
        self.assertEqual(remove_Occ("hello", ""), "hello")
        self.assertEqual(remove_Occ("", ""), "")

    def test_edge_case_long_string(self):
        long_str = "a" * 1000
        self.assertEqual(remove_Occ(long_str, "a"), "")

    def test_edge_case_single_char_long_string(self):
        long_str = "a" * 1000 + "b"
        self.assertEqual(remove_Occ(long_str, "a"), "b")

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, remove_Occ, 123, "a")
        self.assertRaises(TypeError, remove_Occ, "abc", 123)
