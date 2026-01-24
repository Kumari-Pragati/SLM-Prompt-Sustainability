import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, 3), 4)
        self.assertEqual(find_FirstMissing([1, 2, 3], 1, 3), 4)
        self.assertEqual(find_FirstMissing([1, 2, 3], 2, 3), 4)
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, 2), 1)
        self.assertEqual(find_FirstMissing([1, 2, 3], 1, 2), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(find_FirstMissing([], 0, 0), 1)
        self.assertEqual(find_FirstMissing([0], 0, 0), 1)
        self.assertEqual(find_FirstMissing([0], 0, 1), 1)
        self.assertEqual(find_FirstMissing([1], 0, 0), 1)
        self.assertEqual(find_FirstMissing([1], 1, 1), None)
        self.assertEqual(find_FirstMissing([1], 0, 1), 1)
        self.assertEqual(find_FirstMissing([1, 1], 0, 1), 2)
        self.assertEqual(find_FirstMissing([1, 2, 2], 0, 2), 3)
        self.assertEqual(find_FirstMissing([1, 2, 3], 0, 0), None)

    def test_complex(self):
        self.assertEqual(find_FirstMissing([1, 2, 3, 5], 0, 4), 4)
        self.assertEqual(find_FirstMissing([1, 2, 3, 5, 6], 0, 5), 6)
        self.assertEqual(find_FirstMissing([1, 2, 3, 5, 6], 1, 5), 1)
        self.assertEqual(find_FirstMissing([1, 2, 3, 5, 6], 2, 5), 0)
        self.assertEqual(find_FirstMissing([1, 2, 3, 5, 6], 3, 5), 0)
        self.assertEqual(find_FirstMissing([1, 2, 3, 5, 6], 4, 5), 1)
