import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(convert([1, 2, 3, 4]), 1234)

    def test_edge_condition(self):
        self.assertEqual(convert([0]), 0)

    def test_boundary_condition(self):
        self.assertEqual(convert([9, 9, 9, 9, 9]), 99999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            convert("1234")

        with self.assertRaises(TypeError):
            convert(1234)

        with self.assertRaises(TypeError):
            convert([1, 2, "3", 4])
