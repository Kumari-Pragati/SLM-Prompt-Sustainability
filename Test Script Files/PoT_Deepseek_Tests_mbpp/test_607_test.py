import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

    def test_edge_case_pattern_at_start(self):
        self.assertEqual(find_literals('fox quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 0, 3))

    def test_edge_case_pattern_at_end(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog. fox', 'fox'), ('fox', 50, 53))

    def test_edge_case_pattern_not_found(self):
        self.assertIsNone(find_literals('The quick brown jumps over the lazy dog.', 'fox'))

    def test_boundary_case_empty_text(self):
        self.assertIsNone(find_literals('', 'fox'))

    def test_boundary_case_empty_pattern(self):
        self.assertIsNone(find_literals('The quick brown fox jumps over the lazy dog.', ''))

    def test_corner_case_pattern_same_as_text(self):
        self.assertEqual(find_literals('fox', 'fox'), ('fox', 0, 3))

    def test_corner_case_pattern_longer_than_text(self):
        self.assertIsNone(find_literals('fox', 'foxx'))
