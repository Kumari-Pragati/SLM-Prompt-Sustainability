import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)

    def test_edge_case_zero_array(self):
        self.assertEqual(min_jumps([0], 1), 0)

    def test_edge_case_zero_jump(self):
        self.assertEqual(min_jumps([1, 0, 1, 1, 1], 5), float('inf'))

    def test_edge_case_single_element_array(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(min_jumps([], 0), float('inf'))

    def test_edge_case_single_element_array_with_zero_jump(self):
        self.assertEqual(min_jumps([0], 1), float('inf'))

    def test_edge_case_array_with_zero_jump(self):
        self.assertEqual(min_jumps([0, 1, 1, 1, 1], 5), float('inf'))

    def test_edge_case_array_with_zero_jump_and_zero_array(self):
        self.assertEqual(min_jumps([0, 0, 1, 1, 1], 5), float('inf'))

    def test_edge_case_array_with_zero_jump_and_zero_array_and_zero_jump(self):
        self.assertEqual(min_jumps([0, 0, 0, 1, 1], 5), float('inf'))
