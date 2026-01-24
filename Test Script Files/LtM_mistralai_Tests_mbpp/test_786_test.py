import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(right_insertion([1, 3, 5], 2), 1)
        self.assertEqual(right_insertion([1, 3, 5], 4), 2)
        self.assertEqual(right_insertion([1, 3, 5], 6), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(right_insertion([], 1), 0)
        self.assertEqual(right_insertion([1], 1), 0)
        self.assertEqual(right_insertion([1], 2), 1)
        self.assertEqual(right_insertion([1, 1], 1), 1)
        self.assertEqual(right_insertion([1, 1], 2), 2)
        self.assertEqual(right_insertion([1, 1], 3), 2)
        self.assertEqual(right_insertion([1, 1, 1], 1), 0)
        self.assertEqual(right_insertion([1, 1, 1], 2), 3)
        self.assertEqual(right_insertion([1, 1, 1], 4), 3)

    def test_complex(self):
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 0), 0)
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 1), 1)
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 2), 5)
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 3), 6)
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 4), 7)
        self.assertEqual(right_insertion([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 5), 8)
