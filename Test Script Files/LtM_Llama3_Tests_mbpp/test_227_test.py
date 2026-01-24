import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(5, 5, 5), 5)
        self.assertEqual(min_of_three(-1, 0, 1), -1)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(1, 1, 1), 1)
        self.assertEqual(min_of_three(-1, -1, -1), -1)
        self.assertEqual(min_of_three(0, 0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_three('a', 'b', 'c')
        with self.assertRaises(TypeError):
            min_of_three(1, 'b', 3)
        with self.assertRaises(TypeError):
            min_of_three(1, 2, 'c')
