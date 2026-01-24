import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_edge_cases(self):
        self.assertEqual(add_lists([], ()), ())
        self.assertEqual(add_lists([1, 2, 3], ()), (1, 2, 3))

    def test_boundary_cases(self):
        self.assertEqual(add_lists([1, 2], (3, 4)), (3, 4, 1, 2))
        self.assertEqual(add_lists([1, 2, 3, 4, 5], ()), (1, 2, 3, 4, 5))

    def test_special_cases(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6, 7, 8)), (4, 5, 6, 7, 8, 1, 2, 3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_lists('abc', (1, 2, 3))
        with self.assertRaises(TypeError):
            add_lists([1, 2, 3], 'abc')
