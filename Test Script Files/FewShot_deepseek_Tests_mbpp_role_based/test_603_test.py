import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_ludic(10), [1, 4, 7, 10])

    def test_boundary_conditions(self):
        self.assertEqual(get_ludic(1), [1])
        self.assertEqual(get_ludic(0), [])

    def test_edge_cases(self):
        self.assertEqual(get_ludic(2), [1, 2])
        self.assertEqual(get_ludic(3), [1, 3])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_ludic('10')
        with self.assertRaises(ValueError):
            get_ludic(-10)
