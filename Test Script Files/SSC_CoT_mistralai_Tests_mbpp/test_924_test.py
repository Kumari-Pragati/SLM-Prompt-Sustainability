import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(-2, -5), -2)
        self.assertEqual(max_of_two(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(float('inf'), 0), float('inf'))
        self.assertEqual(max_of_two(-float('inf'), 0), -float('inf'))
        self.assertEqual(max_of_two(0, float('nan')), 0)
        self.assertEqual(max_of_two(float('nan'), 0), float('nan'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_two('a', 'b')
        with self.assertRaises(TypeError):
            max_of_two([1, 2, 3], [4, 5, 6])
