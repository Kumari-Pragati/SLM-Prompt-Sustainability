import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list(self):
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5]), [5.0, 5.0, 6.0])
        self.assertEqual(div_list([10, 20, 30], [0, 0, 0]), [None, None, None])
        self.assertEqual(div_list([10, 20, 30], [2, 4, 0]), [5.0, 5.0, None])
        self.assertEqual(div_list([10, 20, 30], [2, 0, 5]), [5.0, None, 6.0])
        self.assertEqual(div_list([10, 20, 30], [0, 2, 5]), [None, 10.0, 6.0])
        self.assertEqual(div_list([10, 20, 30], [2, 4, 5, 6]), [5.0, 5.0, 6.0, float('inf')])

    def test_div_list_empty_list(self):
        self.assertEqual(div_list([], []), [])

    def test_div_list_single_element(self):
        self.assertEqual(div_list([10], [2]), [5.0])
        self.assertEqual(div_list([10], [0]), [None])
        self.assertEqual(div_list([10], [2, 3]), [5.0, float('inf')])

    def test_div_list_single_element_zero(self):
        self.assertEqual(div_list([10], [0]), [None])

    def test_div_list_single_element_zero_list(self):
        self.assertEqual(div_list([10, 20, 30], [0, 0, 0]), [None, None, None])
