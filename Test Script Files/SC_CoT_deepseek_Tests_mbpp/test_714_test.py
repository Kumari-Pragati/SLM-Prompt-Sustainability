import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Fac(10), 4)

    def test_edge_case(self):
        self.assertEqual(count_Fac(1), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Fac(2), 1)

    def test_corner_case(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(-1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Fac('abc')
        with self.assertRaises(TypeError):
            count_Fac(None)
