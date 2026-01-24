import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 3])

    def test_boundary_conditions(self):
        self.assertEqual(get_ludic(0), [])
        self.assertEqual(get_ludic(4), [1, 4])

    def test_edge_cases(self):
        self.assertEqual(get_ludic(5), [1, 5])
        self.assertEqual(get_ludic(6), [1, 3, 5])
        self.assertEqual(get_ludic(7), [1, 3, 5, 7])
        self.assertEqual(get_ludic(8), [1, 3, 5, 7])
        self.assertEqual(get_ludic(9), [1, 3, 7])
        self.assertEqual(get_ludic(10), [1, 3, 7, 9])
