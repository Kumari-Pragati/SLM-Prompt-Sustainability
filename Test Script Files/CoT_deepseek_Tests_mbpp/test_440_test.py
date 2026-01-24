import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        text = "happily ever after"
        self.assertEqual(find_adverb_position(text), (7, 11, 'happily'))

    def test_edge_case_no_adverb(self):
        text = "without any adverbs"
        self.assertIsNone(find_adverb_position(text))

    def test_edge_case_adverb_at_start(self):
        text = "happily ever after"
        self.assertEqual(find_adverb_position(text), (0, 4, 'happily'))

    def test_edge_case_adverb_at_end(self):
        text = "without any adverbs"
        self.assertIsNone(find_adverb_position(text))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)
