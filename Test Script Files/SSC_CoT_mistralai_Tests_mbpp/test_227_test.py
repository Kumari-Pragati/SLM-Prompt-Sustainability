import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(-1, 0, 2), -1)
        self.assertEqual(min_of_three(0, -1, 1), -1)
        self.assertEqual(min_of_three(-1, 0, -2), -2)
        self.assertEqual(min_of_three(0, -1, -2), -2)
        self.assertEqual(min_of_three(-2, -1, 0), -2)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(float('inf'), 1, 2), 1)
        self.assertEqual(min_of_three(-float('inf'), -1, -2), -2)
        self.assertEqual(min_of_three(1, float('inf'), 2), 1)
        self.assertEqual(min_of_three(-1, -float('inf'), -2), -2)
        self.assertEqual(min_of_three(float('inf'), float('inf'), 1), float('inf'))
        self.assertEqual(min_of_three(-float('inf'), -float('inf'), -1), -float('inf'))
