import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(number_of_substrings("abc"), 11)
        self.assertEqual(number_of_substrings("a"), 1)
        self.assertEqual(number_of_substrings("aa"), 2)
        self.assertEqual(number_of_substrings("aaaa"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings("1234567890"), 45)
        self.assertEqual(number_of_substrings("01234567890"), 45)
        self.assertEqual(number_of_substrings("12345678901"), 55)

    def test_special_cases(self):
        self.assertEqual(number_of_substrings("ab"), 6)
        self.assertEqual(number_of_substrings("aabb"), 11)
        self.assertEqual(number_of_substrings("aaaabb"), 20)
        self.assertEqual(number_of_substrings("aaaabbaa"), 16)
