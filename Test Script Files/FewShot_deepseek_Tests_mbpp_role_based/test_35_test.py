import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_rect_num(5), 30)

    def test_boundary_condition(self):
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            find_rect_num(-5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_rect_num(5.5)
