import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11), 3)

    def test_edge_condition_empty_input(self):
        self.assertEqual(min_jumps([], 0), float('inf'))

    def test_edge_condition_single_element(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_edge_condition_zero_in_array(self):
        self.assertEqual(min_jumps([0, 1, 2, 3], 4), float('inf'))

    def test_boundary_condition_maximum_value(self):
        self.assertEqual(min_jumps([10000]*10000, 10000), 10000)

    def test_complex_input(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
