import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(10, 20, 15), 20)
        self.assertEqual(max_of_three(-1, 0, 1), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_of_three(0, 0, 0), 0)
        self.assertEqual(max_of_three(-1000000000, 1000000000, 0), 1000000000)
        self.assertEqual(max_of_three(float('-inf'), float('inf'), 0), float('inf'))

    def test_corner_cases(self):
        self.assertEqual(max_of_three(float('nan'), 1, float('nan')), float('nan'))
        self.assertEqual(max_of_three(float('inf'), float('-inf'), 0), float('inf'))
