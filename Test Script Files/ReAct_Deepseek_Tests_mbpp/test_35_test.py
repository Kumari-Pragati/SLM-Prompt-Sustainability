import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_rect_num(1), 2)
        self.assertEqual(find_rect_num(2), 6)
        self.assertEqual(find_rect_num(3), 12)
        self.assertEqual(find_rect_num(4), 20)

    def test_edge_cases(self):
        self.assertEqual(find_rect_num(0), 0)
        self.assertEqual(find_rect_num(-1), 0)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, this test is empty.
        pass
