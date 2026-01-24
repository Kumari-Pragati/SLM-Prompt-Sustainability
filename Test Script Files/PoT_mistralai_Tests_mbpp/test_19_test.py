import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))
        self.assertTrue(test_duplicate([5, 5, 6, 7, 8]))

    def test_edge(self):
        self.assertFalse(test_duplicate([]))
        self.assertFalse(test_duplicate([1]))
        self.assertTrue(test_duplicate([1, 1]))

    def test_corner(self):
        self.assertFalse(test_duplicate(set([1, 2, 2, 3, 4])))
        self.assertFalse(test_duplicate([float('nan'), float('nan')]))
        self.assertFalse(test_duplicate([True, True]))
