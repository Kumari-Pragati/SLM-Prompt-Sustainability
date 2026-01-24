import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Rotations("hello"), 5)

    def test_edge_case_empty_string(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(find_Rotations("a"), 1)

    def test_edge_case_two_character_string(self):
        self.assertEqual(find_Rotations("ab"), 2)

    def test_edge_case_long_string(self):
        self.assertEqual(find_Rotations("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_edge_case_rotations_of_a_palindrome(self):
        self.assertEqual(find_Rotations("radar"), 2)

    def test_edge_case_rotations_of_a_non_palindrome(self):
        self.assertEqual(find_Rotations("hello world"), 5)
