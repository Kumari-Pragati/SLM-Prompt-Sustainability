import unittest
from mbpp_611_code import max_of_nth

class TestMaxOfNth(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_of_nth([(1, 2), (3, 4), (5, 6)], 1), 2)
        self.assertEqual(max_of_nth([(10, 20), (30, 40), (50, 60)], 0), 10)
        self.assertEqual(max_of_nth([(100, 200), (300, 400), (500, 600)], 2), 600)

    def test_edge_cases(self):
        self.assertEqual(max_of_nth([], 0), None)
        self.assertEqual(max_of_nth([(1, 2)], 1), 2)
        self.assertEqual(max_of_nth([(1, 2), (3, 2)], 1), 2)
        self.assertEqual(max_of_nth([(1, 2), (3, 2)], 2), 2)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            max_of_nth([(1, 2), (3, 4)], -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_of_nth(123, 0)
        with self.assertRaises(TypeError):
            max_of_nth([(1, 2)], 'a')
