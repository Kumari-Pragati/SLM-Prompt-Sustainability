import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_assign_freq(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), "[(1, 1), (2, 2), (3, 3)]")
        self.assertEqual(assign_freq(['a', 'b', 'b', 'c', 'c', 'c']), "[(a, 1), (b, 2), (c, 3)]")
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3, 3]), "[(1, 2), (2, 2), (3, 3)]")
        self.assertEqual(assign_freq(['a', 'a', 'b', 'b', 'c', 'c', 'c']), "[(a, 2), (b, 2), (c, 3)]")
        self.assertEqual(assign_freq([1, 2, 3, 4, 5]), "[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]")
