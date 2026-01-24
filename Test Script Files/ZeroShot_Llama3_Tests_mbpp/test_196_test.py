import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_remove_tuples(self):
        self.assertEqual(remove_tuples([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 3), [1, 2])
        self.assertEqual(remove_tuples([1, 2, 3], 2), [1, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 4), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 5), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 1, 2), [1, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 2, 1), [1, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 3, 2), [1, 2])
        self.assertEqual(remove_tuples([1, 2, 3], 4, 1), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 0, 1), [1, 2, 3])
        self.assertEqual(remove_tuples([1, 2, 3], 5, 2), [1, 2, 3])
