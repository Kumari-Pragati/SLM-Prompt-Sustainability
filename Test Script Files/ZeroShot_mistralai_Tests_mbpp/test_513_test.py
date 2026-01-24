import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_add_str_empty_list(self):
        self.assertListEqual(add_str([], "test"), ["test"])

    def test_add_str_single_element_list(self):
        self.assertListEqual(add_str([["test"]], "K"), ["test", "K"])

    def test_add_str_multiple_elements_list(self):
        self.assertListEqual(add_str([["test1"], ["test2"], ["test3"]], "K"), ["test1", "test2", "test3", "K"])

    def test_add_str_mixed_types_list(self):
        self.assertListEqual(add_str([["test1"], 1, "test2"], "K"), ["test1", "1", "test2", "K"])
