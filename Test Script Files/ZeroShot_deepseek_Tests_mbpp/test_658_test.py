import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(max_occurrences(['a', 'b', 'b', 'c', 'c', 'c']), 'c')
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2]), 1)
        self.assertEqual(max_occurrences(['a', 'a', 'a', 'b', 'b', 'b']), 'a')
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences(['a']), 'a')
        self.assertEqual(max_occurrences([]), None)
