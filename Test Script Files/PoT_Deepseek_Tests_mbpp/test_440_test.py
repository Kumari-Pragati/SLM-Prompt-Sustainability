import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_adverb_position("happily"), (0, 7, "happily"))

    def test_edge_case(self):
        self.assertEqual(find_adverb_position(""), (None, None, None))

    def test_boundary_case(self):
        self.assertEqual(find_adverb_position("happilyly"), (0, 10, "happilyly"))

    def test_corner_case(self):
        self.assertEqual(find_adverb_position("happiness"), (None, None, None))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_adverb_position(123)
