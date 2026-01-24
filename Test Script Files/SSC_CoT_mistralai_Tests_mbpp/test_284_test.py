import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(check_element([1, 1, 1], 1))
        self.assertTrue(check_element(["apple", "apple", "apple"], "apple"))
        self.assertTrue(check_element([3.14, 3.14, 3.14], 3.14))

    def test_edge_cases(self):
        self.assertFalse(check_element([1, 1, 2], 1))
        self.assertFalse(check_element(["apple", "banana", "apple"], "apple"))
        self.assertFalse(check_element([3.14, 3.15, 3.14], 3.14))

    def test_empty_list(self):
        self.assertFalse(check_element([]))

    def test_single_element(self):
        self.assertTrue(check_element([1]))
        self.assertTrue(check_element(["apple"]))
        self.assertTrue(check_element([3.14]))

    def test_none_and_empty_element(self):
        self.assertFalse(check_element([None], None))
        self.assertFalse(check_element([""], ""))
        self.assertFalse(check_element([], None))
