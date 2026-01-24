import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_remove_list_range(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 4), [[3, 4]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 1, 6), [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 3, 5), [[3, 4]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 0, 0), [])
        self.assertEqual(remove_list_range([], 1, 6), [])
