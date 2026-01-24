import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(min_jumps([], 0), float('inf'))

    def test_single_element_array(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_zero_jumps(self):
        self.assertEqual(min_jumps([0, 1, 2, 3], 4), 2)

    def test_no_jumps(self):
        self.assertEqual(min_jumps([1, 2, 3, 4], 4), float('inf'))

    def test_jumps(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)

    def test_jumps_with_zero(self):
        self.assertEqual(min_jumps([0, 1, 2, 3, 4], 5), 2)

    def test_jumps_with_zero_at_end(self):
        self.assertEqual(min_jumps([1, 2, 3, 0, 4], 5), 3)

    def test_jumps_with_zero_at_start(self):
        self.assertEqual(min_jumps([0, 1, 2, 3, 4], 5), 2)

    def test_jumps_with_zero_at_start_and_end(self):
        self.assertEqual(min_jumps([0, 1, 2, 3, 0], 5), 2)
