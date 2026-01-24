import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['a', 'd', 'e']
        self.assertTrue(check_element(test_tup, check_list))

    def test_edge_condition(self):
        test_tup = ()
        check_list = ['a', 'd', 'e']
        self.assertFalse(check_element(test_tup, check_list))

    def test_boundary_condition(self):
        test_tup = ('a',)
        check_list = ['a', 'd', 'e']
        self.assertTrue(check_element(test_tup, check_list))

    def test_invalid_input(self):
        test_tup = ('a', 'b', 'c')
        check_list = ['a', 'd', 'e']
        with self.assertRaises(TypeError):
            check_element(test_tup, 123)
