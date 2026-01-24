import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_typical_case(self):
        text = "I am happily running."
        self.assertEqual(find_adverbs(text), '10-12: happily')

    def test_edge_case(self):
        text = "I am happily running."
        self.assertEqual(find_adverbs(text), '10-12: happily')

    def test_corner_case(self):
        text = "I am happily running, but I am not happily sitting."
        self.assertEqual(find_adverbs(text), '10-12: happily')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverbs(123)
