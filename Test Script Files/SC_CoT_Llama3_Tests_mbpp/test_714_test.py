import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Fac(10), 2)
        self.assertEqual(count_Fac(12), 3)
        self.assertEqual(count_Fac(15), 3)

    def test_edge_cases(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 2)

    def test_special_cases(self):
        self.assertEqual(count_Fac(7), 1)
        self.assertEqual(count_Fac(8), 2)
        self.assertEqual(count_Fac(9), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Fac("a")
        with self.assertRaises(TypeError):
            count_Fac(None)
