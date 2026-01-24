import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_typical_use_case(self):
        text = "happily ever after"
        self.assertEqual(find_adverb_position(text), (7, 11, 'happily'))

    def test_edge_condition(self):
        text = "happily"
        self.assertEqual(find_adverb_position(text), (0, 7, 'happily'))

    def test_boundary_condition(self):
        text = "happilyly"
        self.assertEqual(find_adverb_position(text), (0, 8, 'happilyly'))

    def test_no_adverb(self):
        text = "without any adverbs"
        self.assertIsNone(find_adverb_position(text))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)
