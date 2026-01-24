import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abccba'), 6)

    def test_single_character(self):
        self.assertEqual(count_Substring_with_equal_ends('a'), 1)

    def test_empty_string(self):
        self.assertEqual(count_Substring_with_equal_ends(''), 0)

    def test_all_same_characters(self):
        self.assertEqual(count_Substring_with_equal_ends('aaaaa'), 15)

    def test_all_different_characters(self):
        self.assertEqual(count_Substring_with_equal_ends('abcdefg'), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Substring_with_equal_ends('a'*31), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Substring_with_equal_ends(12345)

        with self.assertRaises(TypeError):
            count_Substring_with_equal_ends(['a', 'b', 'c'])
