import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(3, 5), 5)
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-5, -3), -3)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(2147483647, 2147483646), 2147483647)
        self.assertEqual(max_of_two(-2147483648, -2147483649), -2147483648)
        self.assertEqual(max_of_two(float('inf'), 0), float('inf'))
        self.assertEqual(max_of_two(0, float('-inf')), 0)

    def test_complex(self):
        self.assertEqual(max_of_two(-5, -4.5), -5)
        self.assertEqual(max_of_two(-0.1, 0), 0)
        self.assertEqual(max_of_two('a', 'b'), 'b')
        self.assertEqual(max_of_two(None, 1), 1)
        self.assertEqual(max_of_two(1, None), 1)
