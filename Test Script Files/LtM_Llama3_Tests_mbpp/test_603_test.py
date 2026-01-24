import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 2, 3])
        self.assertEqual(get_ludic(4), [1, 2, 3, 4])

    def test_edge(self):
        self.assertEqual(get_ludic(0), [])
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_larger(self):
        self.assertEqual(get_ludic(10), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_ludic(20), [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            get_ludic('a')
