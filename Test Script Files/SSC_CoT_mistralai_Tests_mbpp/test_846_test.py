import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 4], 3), 1)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3], 3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([1], [1], 1), 1)
        self.assertEqual(find_platform([1, 2], [2, 1], 2), 1)
        self.assertEqual(find_platform([1, 2, 3], [1, 2, 3, 4], 4), 3)
        self.assertEqual(find_platform([1, 2, 3], [1, 2], 2), 2)
        self.assertEqual(find_platform([1, 2, 3], [3, 2, 1], 3), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_platform, [1, 2, 3], 'not_a_list', 3)
        self.assertRaises(TypeError, find_platform, [1, 2, 3], [], 3)
        self.assertRaises(TypeError, find_platform, [1, 2, 3], [1, 2, 3], 'not_a_number')
