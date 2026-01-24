import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_empty_array(self):
        self.assertGreaterEqual(min_jumps([], 0), float('inf'))

    def test_single_element_array(self):
        for element in [0, 1]:
            self.assertEqual(min_jumps([element], 1), 0)

    def test_array_with_zero_at_end(self):
        self.assertGreaterEqual(min_jumps([1, 2, 0], 3), 2)

    def test_array_with_zero_in_middle(self):
        self.assertGreaterEqual(min_jumps([1, 0, 2], 3), 1)

    def test_array_with_multiple_zeros(self):
        self.assertGreaterEqual(min_jumps([1, 0, 1, 0, 1], 5), 2)

    def test_large_array(self):
        arr = [1] * 1000 + [0]
        self.assertGreaterEqual(min_jumps(arr, len(arr)), 999)

    def test_negative_elements(self):
        self.assertRaises(ValueError, min_jumps, [-1, -2, 0], 3)

    def test_negative_array_length(self):
        self.assertRaises(ValueError, min_jumps, [1, 2, 3], -1)
