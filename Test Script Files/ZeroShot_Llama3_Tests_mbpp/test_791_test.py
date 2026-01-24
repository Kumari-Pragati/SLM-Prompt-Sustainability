import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_remove_nested(self):
        self.assertEqual(remove_nested((1, 2, 3)), (1, 2, 3))
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 2, 3, 4))
        self.assertEqual(remove_nested((1, (2, 3), (4, 5), 6)), (1, 2, 3, 4, 5, 6))
        self.assertEqual(remove_nested((1, (2, 3), (4, 5), (6, 7), 8)), (1, 2, 3, 4, 5, 6, 7, 8))
        self.assertEqual(remove_nested((1, (2, 3), (4, 5), (6, 7), (8, 9), 10)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
        self.assertEqual(remove_nested((1, (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), 12)), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
