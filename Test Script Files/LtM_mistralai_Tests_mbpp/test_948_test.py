import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)
        self.assertEqual(get_item(('a', 'b', 'c'), 1), 'b')

    def test_edge_and_boundary(self):
        self.assertEqual(get_item((1,), 0), 1)
        self.assertEqual(get_item((), None), None)
        self.assertEqual(get_item((1, 2, 3), -1), None)
        self.assertEqual(get_item((1, 2, 3), 3), 3)

    def test_complex_input(self):
        self.assertEqual(get_item((1, 2, 3, 4), 2 if 3 < 5 else 1), 2)
        self.assertEqual(get_item((1, 2, 3, 4), 'invalid_index'), None)
