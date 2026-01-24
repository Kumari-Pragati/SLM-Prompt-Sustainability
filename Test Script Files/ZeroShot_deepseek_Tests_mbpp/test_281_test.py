import unittest
from mbpp_281_code import all_unique

class TestAllUnique(unittest.TestCase):

    def test_all_unique_true(self):
        self.assertTrue(all_unique([1, 2, 3, 4, 5]))
        self.assertTrue(all_unique(['a', 'b', 'c', 'd']))
        self.assertTrue(all_unique(['a', 'b', 'a', 'c']))

    def test_all_unique_false(self):
        self.assertFalse(all_unique([1, 2, 2, 3, 4]))
        self.assertFalse(all_unique(['a', 'b', 'b', 'c']))
        self.assertFalse(all_unique(['a', 'a', 'b', 'c']))
