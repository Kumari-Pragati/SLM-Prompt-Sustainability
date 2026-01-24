import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(find_adverb_position("Hello worldly goodbye"), ((6, 13, "worldly")))

    def test_empty_input(self):
        self.assertIsNone(find_adverb_position(""))

    def test_no_adverb(self):
        self.assertIsNone(find_adverb_position("Hello world goodbye"))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("Hello worldly goodbye happily"), ((6, 13, "worldly"), (17, 24, "happily")))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            find_adverb_position([1, 2, 3])
