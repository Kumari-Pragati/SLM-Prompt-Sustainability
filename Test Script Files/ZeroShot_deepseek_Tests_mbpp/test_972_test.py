import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_concatenate_nested(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))
        self.assertEqual(concatenate_nested(('a', 'b'), ('c', 'd')), ('a', 'b', 'c', 'd'))
        self.assertEqual(concatenate_nested(([1, 2], [3, 4]), ([5, 6], [7, 8])), ([1, 2], [3, 4], [5, 6], [7, 8]))
        self.assertEqual(concatenate_nested(({'a': 1}, {'b': 2}), ({'c': 3}, {'d': 4})), (({'a': 1}, {'b': 2}), ({'c': 3}, {'d': 4})))
