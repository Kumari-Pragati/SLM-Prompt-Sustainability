import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([2, 3, 0, 1, 4], 5), 2)
        self.assertEqual(min_jumps([2, 3, 1, 1, 0], 5), float('inf'))
        self.assertEqual(min_jumps([0, 0, 0, 0, 0], 5), float('inf'))

    def test_empty_list(self):
        self.assertEqual(min_jumps([], 0), 0)

    def test_single_element(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(min_jumps([-1, -2, -3], 3), float('inf'))

    def test_zero_array(self):
        self.assertEqual(min_jumps([0], 1), 0)
