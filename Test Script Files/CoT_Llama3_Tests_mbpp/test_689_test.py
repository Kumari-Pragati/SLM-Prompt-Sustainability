import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_min_jumps_zero(self):
        self.assertEqual(min_jumps([0, 1, 2, 3], 4), float('inf'))

    def test_min_jumps_single_element(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_min_jumps_all_zeros(self):
        self.assertEqual(min_jumps([0, 0, 0, 0], 4), float('inf'))

    def test_min_jumps_all_ones(self):
        self.assertEqual(min_jumps([1, 1, 1, 1], 4), 3)

    def test_min_jumps_random(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)

    def test_min_jumps_edge_case(self):
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 4)
