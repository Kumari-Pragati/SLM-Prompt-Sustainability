import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 4], 4), None)
        self.assertEqual(find_Extra([1, 1, 2, 3], [1, 2, 2, 4], 4), 2)
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 3, 2, 4], 4), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Extra([], [], 0), None)
        self.assertEqual(find_Extra([1], [1], 1), None)
        self.assertEqual(find_Extra([1, 2], [1, 2, 3], 3), 2)
        self.assertEqual(find_Extra([1, 2, 3], [1, 2, 3, 4], 4), None)
        self.assertEqual(find_Extra([1, 2, 3], [1, 2, 3, 4, 5], 5), 4)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Extra, [1, 2, 3], 'arr2', 3)
        self.assertRaises(TypeError, find_Extra, [1, 2, 3], [1, 2, 3], 'n')
        self.assertRaises(TypeError, find_Extra, [1, 2, 3], [1, 2, 3], -1)
