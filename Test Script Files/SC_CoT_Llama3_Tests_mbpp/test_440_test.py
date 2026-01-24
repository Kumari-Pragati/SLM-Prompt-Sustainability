import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly"), ((12, 19, "slowly")))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly and quietly"), ((12, 19, "slowly"), (24, 31, "quietly")))

    def test_no_adverbs(self):
        self.assertIsNone(find_adverb_position("I am going to the store"))

    def test_edge_case(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly quickly"), ((12, 19, "slowly"), (20, 27, "quickly")))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)

    def test_empty_string(self):
        self.assertIsNone(find_adverb_position(""))

    def test_single_character(self):
        self.assertIsNone(find_adverb_position("a"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position({"a": "b"})
