import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 10)

    def test_edge_cases(self):
        self.assertEqual(find_rect_num(-1), 0)
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(100), 10100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_rect_num("a")
        with self.assertRaises(TypeError):
            find_rect_num(None)
