import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(right_insertion([1, 2, 3, 4], 2), 2)
        self.assertEqual(right_insertion([1, 2, 3, 4], 5), 4)
        self.assertEqual(right_insertion([], 1), 0)
        self.assertEqual(right_insertion([1], 1), 1)
        self.assertEqual(right_insertion([1, 1], 1), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(right_insertion([1, 2, 3], 0), 0)
        self.assertEqual(right_insertion([1, 2, 3], -1), 0)
        self.assertEqual(right_insertion([1, 2, 3], float('inf')), 4)
