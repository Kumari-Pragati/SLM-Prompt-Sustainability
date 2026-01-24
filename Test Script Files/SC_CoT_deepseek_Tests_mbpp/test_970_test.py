import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_two(3, 5), 3)
        self.assertEqual(min_of_two(7, 2), 2)

    def test_edge_cases(self):
        self.assertEqual(min_of_two(0, 0), 0)
        self.assertEqual(min_of_two(-1, -1), -1)
        self.assertEqual(min_of_two(float('-inf'), float('inf')), float('-inf'))

    def test_corner_cases(self):
        self.assertEqual(min_of_two(float('inf'), float('-inf')), float('-inf'))
        self.assertEqual(min_of_two(float('nan'), 1), float('nan'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_two(None, None)
        with self.assertRaises(TypeError):
            min_of_two('a', 'b')
