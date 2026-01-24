import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_of_nth([[1], [2], [3]], 0), 1)
        self.assertEqual(max_of_nth([[1], [2], [3]], 1), 2)
        self.assertEqual(max_of_nth([[1], [2], [3]], 2), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(max_of_nth([], 0), None)
        self.assertEqual(max_of_nth([[1]], 0), 1)
        self.assertEqual(max_of_nth([[1], [2]], 1), 2)
        self.assertEqual(max_of_nth([[1], [2]], 2), None)
        self.assertEqual(max_of_nth([[1, float('inf')], [2, float('inf')]], 0), float('inf'))
        self.assertEqual(max_of_nth([[1, -1], [2, -1]], 0), -1)

    def test_complex(self):
        self.assertEqual(max_of_nth([[1], [2, 3], [4, 5, 6]], 1), 3)
        self.assertEqual(max_of_nth([[1], [2, 3], [4, 5, 6]], 2), 6)
        self.assertEqual(max_of_nth([[1, 2], [3, 4], [5, 6]], 0), 1)
        self.assertEqual(max_of_nth([[1, 2], [3, 4], [5, 6]], 1), 2)
        self.assertEqual(max_of_nth([[1, 2], [3, 4], [5, 6]], 2), 6)
