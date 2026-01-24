import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 4, 6]), [0, 5, 5])

    def test_edge_case_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            moddiv_list([10, 20, 30], [0, 4, 6])

    def test_edge_case_with_single_element(self):
        self.assertEqual(moddiv_list([10], [2]), [0])

    def test_empty_lists(self):
        self.assertEqual(moddiv_list([], []), [])

    def test_negative_numbers(self):
        self.assertEqual(moddiv_list([-10, -20, -30], [2, 4, 6]), [0, 0, 0])
