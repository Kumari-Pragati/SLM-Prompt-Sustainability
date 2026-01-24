import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(right_insertion([1, 3, 5], 2), 2)
        self.assertEqual(right_insertion([10, 20, 30, 40], 25), 3)

    def test_edge_cases(self):
        self.assertEqual(right_insertion([], 1), 0)
        self.assertEqual(right_insertion([1], 1), 1)
        self.assertEqual(right_insertion([1, 2], 3), 2)
        self.assertEqual(right_insertion([1, 2], 0), 0)
        self.assertEqual(right_insertion([1, 2], float('inf')), len([1, 2]) + 1)

    def test_boundary_conditions(self):
        self.assertEqual(right_insertion([0, 1, 2], 0), 0)
        self.assertEqual(right_insertion([-1, 0, 1], -1), 0)
        self.assertEqual(right_insertion([1, 2, 3], 4), len([1, 2, 3]) + 1)
        self.assertEqual(right_insertion([-1, -2, -3], -4), len([-1, -2, -3]) + 1)
