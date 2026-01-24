import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(min_jumps([], 0), float('inf'))

    def test_single_element_array(self):
        self.assertEqual(min_jumps([1], 1), 0)

    def test_zero_jumps(self):
        self.assertEqual(min_jumps([1, 2, 3], 3), 2)

    def test_no_jumps(self):
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 4)

    def test_jumps(self):
        self.assertEqual(min_jumps([1, 2, 3, 4, 5, 6], 6), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_jumps("abc", 0)
