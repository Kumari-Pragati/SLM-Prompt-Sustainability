import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_typical_case(self):
        text = "I am happily running"
        self.assertEqual(find_adverbs(text), '10-12: happily')

    def test_no_adverb(self):
        text = "I am running"
        self.assertIsNone(find_adverbs(text))

    def test_edge_case_start(self):
        text = "happily running"
        self.assertEqual(find_adverbs(text), '0-2: happily')

    def test_edge_case_end(self):
        text = "I am happily"
        self.assertEqual(find_adverbs(text), '10-12: happily')

    def test_edge_case_whole_text(self):
        text = "happily"
        self.assertEqual(find_adverbs(text), '0-2: happily')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverbs(123)
