import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(div_list([10, 20, 30], [1, 2, 3]), [10.0, 10.0, 10.0])

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [0, 2, 3])

    def test_edge_case_empty_lists(self):
        self.assertEqual(div_list([], []), [])
        self.assertEqual(div_list([], [1, 2, 3]), [])
        self.assertEqual(div_list([1, 2, 3], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(div_list([10], [1]), [10])
        self.assertEqual(div_list([10], [0]), [float('inf')])

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(div_list([10, 20, 30], [1, 2, None]), [10, 10, None])
        self.assertEqual(div_list([10, 20, 30], [1, 2, 'a']), [10, 10, 'a'])
