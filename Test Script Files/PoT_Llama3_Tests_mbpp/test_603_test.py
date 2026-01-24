import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])

    def test_boundary_case(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_larger_input(self):
        self.assertEqual(get_ludic(20), list(range(1, 21)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic('a')
