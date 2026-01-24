import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))
        self.assertTrue(all_unique(['a', 'b', 'c', 'd']))
        self.assertTrue(all_unique(['a', 'b', 'a', 'b']))

    def test_edge_cases(self):
        self.assertTrue(all_unique([]))
        self.assertTrue(all_unique(['a']))

    def test_boundary_cases(self):
        self.assertFalse(all_unique([1, 1]))
        self.assertFalse(all_unique(['a', 'a']))

    def test_corner_cases(self):
        self.assertFalse(all_unique([1, 2, 3, 1]))
        self.assertFalse(all_unique(['a', 'b', 'c', 'a']))
