import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 1), 2)
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 0), 2)
        self.assertEqual(min_Num([], 0), 2)

    def test_special_cases(self):
        self.assertEqual(min_Num([1, 1, 1, 1, 1], 5), 2)
        self.assertEqual(min_Num([2, 2, 2, 2, 2], 5), 2)
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_Num('abc', 5)
        with self.assertRaises(TypeError):
            min_Num([1, 2, 3], 'abc')
