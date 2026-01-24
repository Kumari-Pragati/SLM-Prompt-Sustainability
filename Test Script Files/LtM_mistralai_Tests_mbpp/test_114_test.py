import unittest
from mbpp_114_code import Counter
from 114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3]), '[("1", "1"), ("2", "2"), ("3", "2")]')
        self.assertEqual(assign_freq([4, 4, 4, 5, 5, 5]), '[("4", "3"), ("5", "3")]')

    def test_edge_and_boundary(self):
        self.assertEqual(assign_freq([1]), '[("1", "1")]')
        self.assertEqual(assign_freq([1, 1, 1]), '[("1", "3")]')
        self.assertEqual(assign_freq([1, 2, 3, 4, 5]), '[("1", "1"), ("2", "1"), ("3", "1"), ("4", "1"), ("5", "1")]')
        self.assertEqual(assign_freq([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]), '[("1", "1"), ("2", "3"), ("3", "3"), ("4", "3"), ("5", "4")]')

    def test_complex(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 2, 2]), '[("1", "1"), ("2", "4"), ("3", "3")]')
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 1, 1]), '[("1", "4"), ("2", "3"), ("3", "4"), ("4", "4"), ("5", "4")]')
