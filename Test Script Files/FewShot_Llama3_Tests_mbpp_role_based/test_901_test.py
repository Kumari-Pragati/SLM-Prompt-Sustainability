import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple_of_small_numbers(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 60)

    def test_smallest_multiple_of_large_numbers(self):
        self.assertEqual(smallest_multiple(10), 2520)
        self.assertEqual(smallest_multiple(20), 232792560)
        self.assertEqual(smallest_multiple(30), 232792560)

    def test_smallest_multiple_of_edge_cases(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)

    def test_smallest_multiple_of_invalid_inputs(self):
        with self.assertRaises(TypeError):
            smallest_multiple("a")
