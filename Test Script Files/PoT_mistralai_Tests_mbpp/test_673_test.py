import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)

    def test_edge_case_single_digit(self):
        self.assertEqual(convert([1]), 1)
        self.assertEqual(convert([9]), 9)

    def test_edge_case_zero(self):
        self.assertEqual(convert([]), 0)
        self.assertEqual(convert([0]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(convert([-1, -2, -3]), 321)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(convert([1, -2, 3]), 6)

    def test_corner_case_empty_list(self):
        self.assertEqual(convert([]), 0)
