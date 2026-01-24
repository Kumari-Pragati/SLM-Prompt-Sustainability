import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11), 3)

    def test_single_element(self):
        self.assertEqual(min_jumps([0], 1), float('inf'))

    def test_zero_element(self):
        self.assertEqual(min_jumps([], 0), float('inf'))

    def test_negative_elements(self):
        self.assertEqual(min_jumps([-1, -3, -5, -8, -9, -2, -6, -7, -6, -8, -9], 11), float('inf'))

    def test_zero_in_array(self):
        self.assertEqual(min_jumps([1, 3, 0, 8, 9, 2, 6, 7, 6, 8, 9], 11), 4)

    def test_large_array(self):
        self.assertEqual(min_jumps(list(range(1, 10001)), 10000), 1617)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_jumps("not an array", 10)
