import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_element_present(self):
        test_tup = (1, 2, 3, 4)
        check_list = (1, 2)
        self.assertTrue(check_element(test_tup, check_list))

    def test_element_absent(self):
        test_tup = (1, 2, 3, 4)
        check_list = (5, 6)
        self.assertFalse(check_element(test_tup, check_list))

    def test_element_present_at_start(self):
        test_tup = (1, 2, 3, 4)
        check_list = (1, 3)
        self.assertTrue(check_element(test_tup, check_list))

    def test_element_present_at_end(self):
        test_tup = (1, 2, 3, 4)
        check_list = (3, 4)
        self.assertTrue(check_element(test_tup, check_list))

    def test_element_present_multiple_times(self):
        test_tup = (1, 2, 3, 4)
        check_list = (1, 2, 3)
        self.assertTrue(check_element(test_tup, check_list))

    def test_empty_test_tuple(self):
        test_tup = ()
        check_list = (1, 2)
        self.assertFalse(check_element(test_tup, check_list))

    def test_empty_check_list(self):
        test_tup = (1, 2, 3, 4)
        check_list = ()
        self.assertFalse(check_element(test_tup, check_list))
