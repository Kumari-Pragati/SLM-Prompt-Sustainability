import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple_for_small_numbers(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)

    def test_smallest_multiple_for_larger_numbers(self):
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(6), 12)

    def test_smallest_multiple_for_edge_cases(self):
        self.assertEqual(smallest_multiple(7), 84)
        self.assertEqual(smallest_multiple(8), 16)
        self.assertEqual(smallest_multiple(9), 18)

    def test_smallest_multiple_for_corner_cases(self):
        self.assertEqual(smallest_multiple(10), 20)
        self.assertEqual(smallest_multiple(11), 1326)
        self.assertEqual(smallest_multiple(12), 12)

    def test_smallest_multiple_for_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_multiple('a')
