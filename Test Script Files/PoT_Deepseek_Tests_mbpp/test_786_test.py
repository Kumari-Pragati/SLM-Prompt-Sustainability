import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(right_insertion([1, 3, 5, 7], 5), 2)
        self.assertEqual(right_insertion([1, 3, 5, 7], 8), 4)
        self.assertEqual(right_insertion([1, 3, 5, 7], 0), 0)

    def test_edge_cases(self):
        self.assertEqual(right_insertion([], 5), 0)
        self.assertEqual(right_insertion([1, 3, 5, 7], 1), 0)
        self.assertEqual(right_insertion([1, 3, 5, 7], 7), 3)

    def test_corner_cases(self):
        self.assertEqual(right_insertion([1, 3, 5, 7], 3), 1)
        self.assertEqual(right_insertion([1, 3, 5, 7], 5), 2)
        self.assertEqual(right_insertion([1, 3, 5, 7], 7), 3)
