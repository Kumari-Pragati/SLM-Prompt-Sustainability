import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 4], 4), None)
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 5], 4), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 0], 4), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(find_Extra([], [], 0), None)
        self.assertEqual(find_Extra([1], [1], 1), None)
        self.assertEqual(find_Extra([1, 2], [1, 2, 3], 3), 2)
        self.assertEqual(find_Extra([1, 2], [1, 2], 2), None)

    def test_complex(self):
        self.assertEqual(find_Extra([1, 2, 2, 3], [1, 2, 3, 3], 4), 2)
        self.assertEqual(find_Extra([1, 2, 2, 3], [1, 2, 3, 4], 4), 3)
        self.assertEqual(find_Extra([1, 2, 2, 3], [1, 2, 3, 0], 4), 2)
