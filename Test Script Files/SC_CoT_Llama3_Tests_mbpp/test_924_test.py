import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(7, 7), 7)

    def test_edge_cases(self):
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-5, -10), -5)

    def test_negative_inputs(self):
        self.assertEqual(max_of_two(-5, 3), -5)
        self.assertEqual(max_of_two(-10, -5), -10)

    def test_zero_inputs(self):
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(0, 10), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_two('a', 5)
        with self.assertRaises(TypeError):
            max_of_two(5, 'b')
