import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_ludic(5), [1, 4, 3])

    def test_edge_case_n_equals_1(self):
        self.assertEqual(get_ludic(1), [1])

    def test_boundary_case_n_equals_2(self):
        self.assertEqual(get_ludic(2), [1, 2])

    def test_corner_case_n_equals_3(self):
        self.assertEqual(get_ludic(3), [1, 3, 2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic('5')
