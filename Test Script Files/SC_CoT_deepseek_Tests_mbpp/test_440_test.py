import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        text = "I am running happily"
        self.assertEqual(find_adverb_position(text), (10, 14, 'happily'))

    def test_edge_case(self):
        text = "I am running happily"
        self.assertIsNone(find_adverb_position(text[::-1]))

    def test_corner_case(self):
        text = "I am running happily"
        self.assertIsNone(find_adverb_position(text.replace('happily', 'happilyly')))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)
