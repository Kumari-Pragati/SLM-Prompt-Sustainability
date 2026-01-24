import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [1, 4])
        self.assertEqual(Diff(['a', 'b', 'c'], ['b', 'd', 'c']), ['a', 'd'])

    def test_empty_input(self):
        self.assertEqual(Diff([], []), [])

    def test_single_element_input(self):
        self.assertEqual(Diff([1], []), [1])
        self.assertEqual(Diff([], [1]), [1])

    def test_edge_cases(self):
        self.assertEqual(Diff([1, 1], [2]), [1])
        self.assertEqual(Diff([1], [1]), [])
        self.assertEqual(Diff([1, 2, 1], [2, 1]), [])
        self.assertEqual(Diff([1, 2, 1], [2, 3]), [1])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Diff, 1, 2.5)
        self.assertRaises(TypeError, Diff, '1', '2')
