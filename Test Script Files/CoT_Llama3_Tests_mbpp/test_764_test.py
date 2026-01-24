import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(number_ctr("123abc"), 3)
        self.assertEqual(number_ctr("456def"), 3)
        self.assertEqual(number_ctr("789ghi"), 3)

    def test_edge_cases(self):
        self.assertEqual(number_ctr(""), 0)
        self.assertEqual(number_ctr("abc"), 0)
        self.assertEqual(number_ctr("123456"), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            number_ctr(None)
        with self.assertRaises(TypeError):
            number_ctr(123)

    def test_boundary_conditions(self):
        self.assertEqual(number_ctr("0123456789"), 10)
        self.assertEqual(number_ctr("999999999"), 9)
