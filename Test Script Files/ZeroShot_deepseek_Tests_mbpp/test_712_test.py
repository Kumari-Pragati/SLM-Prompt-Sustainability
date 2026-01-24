import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):

    def test_remove_duplicate(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicate(['a', 'b', 'b', 'c', 'd', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(remove_duplicate([1, 'a', 'a', 2, 2, 'b', 3]), [1, 'a', 2, 'b', 3])
        self.assertEqual(remove_duplicate([]), [])
        self.assertEqual(remove_duplicate([1]), [1])
