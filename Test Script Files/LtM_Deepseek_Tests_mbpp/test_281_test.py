import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(all_unique([1, 2, 3, 4]))
        self.assertTrue(all_unique(['a', 'b', 'c']))
        self.assertTrue(all_unique(['a', 'b', 'a']))

    def test_edge_conditions(self):
        self.assertTrue(all_unique([]))
        self.assertTrue(all_unique(['a']))
        self.assertFalse(all_unique(['a', 'a']))

    def test_complex_cases(self):
        self.assertFalse(all_unique([1, 2, 2, 3]))
        self.assertFalse(all_unique(['a', 'b', 'b', 'c']))
        self.assertFalse(all_unique(['a', 'a', 'b', 'b']))
