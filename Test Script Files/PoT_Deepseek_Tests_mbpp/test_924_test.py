import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_of_two(1, 2), 2)
        self.assertEqual(max_of_two(10, 5), 10)
        self.assertEqual(max_of_two(-1, -2), -1)
        self.assertEqual(max_of_two(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(float('inf'), 1), float('inf'))
        self.assertEqual(max_of_two(-float('inf'), -1), -1)
        self.assertEqual(max_of_two(float('nan'), 1), float('nan'))

    def test_boundary_cases(self):
        self.assertEqual(max_of_two(1, float('inf')), float('inf'))
        self.assertEqual(max_of_two(-1, -float('inf')), -1)
        self.assertEqual(max_of_two(float('nan'), 1), float('nan'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_two(1, 'a')
        with self.assertRaises(TypeError):
            max_of_two('a', 1)
        with self.assertRaises(TypeError):
            max_of_two('a', 'b')
