import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_ludic(5), [1, 3, 7, 9])
        self.assertEqual(get_ludic(10), [1, 3, 7, 9, 19, 23, 29, 31, 47, 59])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1])
        self.assertEqual(get_ludic(4), [1, 3])
        self.assertEqual(get_ludic(6), [1, 3, 7])
        self.assertEqual(get_ludic(20), [1, 3, 7, 9, 19, 23, 29, 31, 47, 59])
        self.assertEqual(get_ludic(30), [1, 3, 7, 9, 19, 23, 29, 31, 47, 53, 59, 71])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic(0)
        with self.assertRaises(TypeError):
            get_ludic(-1)
        with self.assertRaises(TypeError):
            get_ludic('a')
