import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly"), ((15, 24, "slowly")))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly and quickly"), ((15, 24, "slowly"), (27, 36, "quickly")))

    def test_no_adverbs(self):
        self.assertEqual(find_adverb_position("I am going to the store"), [])

    def test_edge_case(self):
        self.assertEqual(find_adverb_position("I am going to the store slowly slowly"), ((15, 24, "slowly"), (25, 34, "slowly")))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)
