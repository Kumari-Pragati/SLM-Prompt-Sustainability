import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_empty_array(self):
        self.assertAlmostEqual(min_jumps([], 0), float('inf'))

    def test_single_element_array(self):
        self.assertAlmostEqual(min_jumps([1], 1), 0)

    def test_simple_array(self):
        self.assertAlmostEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)

    def test_array_with_zero(self):
        self.assertAlmostEqual(min_jumps([2, 3, 0, 1, 4], 5), float('inf'))

    def test_array_with_negative_numbers(self):
        self.assertAlmostEqual(min_jumps([-1, -2, 0, 1, 4], 5), 2)

    def test_large_array(self):
        arr = [i for i in range(100)]
        self.assertAlmostEqual(min_jumps(arr, len(arr)), 99)

    def test_invalid_input_array(self):
        with self.assertRaises(TypeError):
            min_jumps([1, 2, 3], 'invalid')

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            min_jumps([1, 2, 3], 0.5)
