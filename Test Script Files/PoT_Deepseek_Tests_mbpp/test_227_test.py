import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(2, 1, 3), 1)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(-1, -1, -1), -1)
        self.assertEqual(min_of_three(0.5, 0.5, 0.5), 0.5)

    def test_boundary_cases(self):
        self.assertEqual(min_of_three(float('inf'), float('inf'), float('inf')), float('inf'))
        self.assertEqual(min_of_three(-float('inf'), -float('inf'), -float('inf')), -float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_three("1", 2, 3)
        with self.assertRaises(TypeError):
            min_of_three(1, "2", 3)
        with self.assertRaises(TypeError):
            min_of_three(1, 2, "3")
