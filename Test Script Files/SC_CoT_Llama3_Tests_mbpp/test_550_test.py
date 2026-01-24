import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 1, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 1, 4), 5)

    def test_edge_cases(self):
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([1], 0, 1), 1)
        self.assertEqual(find_Max([1, 2], 0, 1), 2)
        self.assertEqual(find_Max([1, 2], 0, 0), 1)

    def test_special_cases(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6], 0, 5), 6)
        self.assertEqual(find_Max([5, 4, 3, 2, 1, 0], 0, 5), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6], 2, 5), 6)
        self.assertEqual(find_Max([5, 4, 3, 2, 1, 0], 2, 5), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Max('abc', 0, 1)
        with self.assertRaises(TypeError):
            find_Max([1, 2, 3], 'abc', 1)
        with self.assertRaises(TypeError):
            find_Max([1, 2, 3], 0, 'abc')
