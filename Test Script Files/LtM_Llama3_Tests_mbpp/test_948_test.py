import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_item((1, 2, 3), 0), 1)
        self.assertEqual(get_item((1, 2, 3), 1), 2)
        self.assertEqual(get_item((1, 2, 3), 2), 3)

    def test_edge(self):
        self.assertEqual(get_item((1, 2, 3), -1), None)
        self.assertEqual(get_item((1, 2, 3), 3), 3)
        self.assertEqual(get_item((1, 2, 3), 4), None)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            get_item(None, 0)
        with self.assertRaises(TypeError):
            get_item((1, 2, 3), 'a')
