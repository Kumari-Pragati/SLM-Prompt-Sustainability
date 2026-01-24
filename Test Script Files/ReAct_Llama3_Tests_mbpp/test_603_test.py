import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 2, 3])

    def test_larger_input(self):
        self.assertEqual(get_ludic(10), list(range(1, 11)))

    def test_larger_input_with_deletions(self):
        self.assertEqual(get_ludic(15), [1, 2, 4, 7, 11, 13, 14, 15])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic('a')
