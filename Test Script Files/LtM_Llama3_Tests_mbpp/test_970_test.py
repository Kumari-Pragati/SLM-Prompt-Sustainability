import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(5, 3), 3)
        self.assertEqual(min_of_two(10, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(-1, 0), -1)
        self.assertEqual(min_of_two(1, float('inf')), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_of_two('a', 2)
        with self.assertRaises(TypeError):
            min_of_two(2, 'b')
