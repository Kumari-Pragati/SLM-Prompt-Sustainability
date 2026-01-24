import unittest
from mbpp_114_code import Counter
from 114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3]), '(1, 2)\n(2, 2)\n(3, 2)')
        self.assertEqual(assign_freq(['a', 'a', 'b', 'b', 'c', 'c']), '(a, 2)\n(b, 2)\n(c, 2)')

    def test_edge_input(self):
        self.assertEqual(assign_freq([1]), '(1, 1)')
        self.assertEqual(assign_freq([1, 1, 1]), '(1, 3)')
        self.assertEqual(assign_freq([1, 2, 1, 2, 1]), '(1, 3)\n(2, 2)')
        self.assertEqual(assign_freq(['a', 'b', 'a', 'b', 'a']), '(a, 3)\n(b, 2)')

    def test_empty_input(self):
        self.assertEqual(assign_freq([]), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            assign_freq(123)
        with self.assertRaises(TypeError):
            assign_freq(('a', 'b'))
