import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(remove_nested((1, 2, 3)), (1, 2, 3))
        self.assertEqual(remove_nested((1, (2, 3), 4)), (1, 2, 3, 4))
        self.assertEqual(remove_nested((1, 2, (3, 4), 5)), (1, 2, 3, 4, 5))

    def test_edge(self):
        self.assertEqual(remove_nested(()), ())
        self.assertEqual(remove_nested((1,)), (1,))
        self.assertEqual(remove_nested((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_corner(self):
        self.assertEqual(remove_nested(((1, 2), 3)), (1, 2, 3))
        self.assertEqual(remove_nested(((1, 2), (3, 4), 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_nested(((1, 2), (3, 4), (5, 6))), (1, 2, 3, 4, 5, 6))
