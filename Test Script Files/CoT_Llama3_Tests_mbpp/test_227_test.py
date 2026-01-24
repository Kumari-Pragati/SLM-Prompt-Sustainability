import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(5, 3, 2), 2)
        self.assertEqual(min_of_three(10, 10, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(-1, -2, -3), -3)
        self.assertEqual(min_of_three(1, 1, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_three('a', 'b', 'c')
        with self.assertRaises(TypeError):
            min_of_three(1, 'b', 'c')
        with self.assertRaises(TypeError):
            min_of_three(1, 2, 'c')
