import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(5, 5, 5), 5)
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(max_of_three(0, -1, -2), 0)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
        self.assertEqual(max_of_three(float('-inf'), float('-inf'), float('-inf')), float('-inf'))

    def test_boundary_conditions(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(2, 3, 4), 4)
        self.assertEqual(max_of_three(float('-inf'), 0, float('inf')), float('inf'))

    def test_complex_cases(self):
        self.assertEqual(max_of_three(100, 200, 300), 300)
        self.assertEqual(max_of_three(-100, -200, -300), -100)
        self.assertEqual(max_of_three(float('inf'), float('-inf'), 0), float('inf'))
