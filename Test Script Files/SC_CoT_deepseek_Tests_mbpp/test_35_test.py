import unittest

from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)
        self.assertEqual(find_rect_num(4), 20)
        self.assertEqual(find_rect_num(5), 30)

    def test_boundary_conditions(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1), 2)

    def test_edge_cases(self):
        self.assertEqual(find_rect_num(-1), 0)
        self.assertEqual(find_rect_num(0.5), 1)
        self.assertEqual(find_rect_num(1.5), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_rect_num('a')
        with self.assertRaises(TypeError):
            find_rect_num(None)
