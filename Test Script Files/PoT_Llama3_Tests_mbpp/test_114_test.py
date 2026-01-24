import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), "[(1, 1), (2, 2), (3, 3)]")

    def test_edge(self):
        self.assertEqual(assign_freq([1, 1, 1, 2, 2, 2, 3, 3, 3]), "[(1, 3), (2, 3), (3, 3)]")

    def test_empty(self):
        self.assertEqual(assign_freq([]), "[]")

    def test_single(self):
        self.assertEqual(assign_freq([1]), "[(1, 1)]")

    def test_duplicates(self):
        self.assertEqual(assign_freq([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]), "[(1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]")
