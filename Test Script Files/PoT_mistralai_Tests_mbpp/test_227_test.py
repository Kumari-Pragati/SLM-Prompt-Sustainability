import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(-1, 0, 1), -1)
        self.assertEqual(min_of_three(0, -1, 1), -1)
        self.assertEqual(min_of_three(0, 0, -1), -1)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(float('inf'), 0, -1), 0)
        self.assertEqual(min_of_three(-1, float('inf'), 0), -1)
        self.assertEqual(min_of_three(float('nan'), 0, 0), 0)
