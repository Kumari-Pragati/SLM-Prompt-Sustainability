import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_empty_list(self):
        self.assertAlmostEqual(min_jumps([], 0), float('inf'))

    def test_single_element(self):
        self.assertAlmostEqual(min_jumps([1], 1), 0)

    def test_multiple_elements_no_jumps(self):
        self.assertAlmostEqual(min_jumps([0, 0, 0], 3), float('inf'))

    def test_multiple_elements_single_jump(self):
        self.assertAlmostEqual(min_jumps([1, 0, 1, 1, 0], 5), 2)

    def test_multiple_elements_multiple_jumps(self):
        self.assertAlmostEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)

    def test_large_input(self):
        self.assertAlmostEqual(min_jumps([2, 3, 1, 1, 4, 2, 5, 6, 3, 4, 1, 2, 0, 3, 1, 2, 1, 3], 20), 3)
