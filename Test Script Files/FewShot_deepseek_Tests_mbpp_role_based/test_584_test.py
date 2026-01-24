import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_use_case(self):
        text = "I am happily running"
        self.assertEqual(find_adverbs(text), '14-17: happily')

    def test_edge_condition(self):
        text = "I am"
        self.assertIsNone(find_adverbs(text))

    def test_boundary_condition(self):
        text = "I am running happily"
        self.assertEqual(find_adverbs(text), '14-17: happily')

    def test_invalid_input(self):
        text = 12345
        with self.assertRaises(TypeError):
            find_adverbs(text)
