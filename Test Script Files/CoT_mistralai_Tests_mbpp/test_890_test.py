import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_find_extra_typical_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], 6), 5)

    def test_find_extra_edge_case_1(self):
        self.assertEqual(find_Extra([], [], 0), 0)
        self.assertEqual(find_Extra([1], [], 1), 0)
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_find_extra_edge_case_2(self):
        self.assertEqual(find_Extra([1, 2], [1], 1), 1)
        self.assertEqual(find_Extra([1, 2], [], 0), 0)

    def test_find_extra_invalid_input(self):
        self.assertRaises(TypeError, find_Extra, [1, 2], 'arr2', 2)
        self.assertRaises(TypeError, find_Extra, [1, 2], [1, 2.5], 2)
        self.assertRaises(TypeError, find_Extra, [1, 2], [1, 2], -1)
