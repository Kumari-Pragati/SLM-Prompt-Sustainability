import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(find_Rotations('a'), 1)

    def test_same_chars(self):
        self.assertEqual(find_Rotations('aaaaa'), 1)

    def test_normal_case(self):
        self.assertEqual(find_Rotations('abcdabcd'), 2)

    def test_empty_string(self):
        self.assertEqual(find_Rotations(''), 0)

    def test_long_string(self):
        self.assertEqual(find_Rotations('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'), 1)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            find_Rotations(12345)
