import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(-2, -1, -3, -4), (-2, -1))
        self.assertEqual(find_Points(0, 0, 5, 5), (-1, 5))
        self.assertEqual(find_Points(5, 5, 0, 0), (0, -1))

    def test_equal_inputs(self):
        self.assertEqual(find_Points(1, 1, 2, 2), (-1, -1))
        self.assertEqual(find_Points(-2, -2, -3, -3), (-1, -1))
        self.assertEqual(find_Points(0, 0, 0, 0), (-1, -1))

    def test_one_input_is_list(self):
        self.assertEqual(find_Points([1], 2, [3], 4), (1, 4))
        self.assertEqual(find_Points(1, [2], [3], 4), (1, 4))
        self.assertEqual(find_Points([1], [2], [3], [4]), (1, 4))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Points, 'a', 2, 'b', 3)
        self.assertRaises(TypeError, find_Points, 1, 'a', 2, 3)
        self.assertRaises(TypeError, find_Points, 1, 2, 'a', 'b')
