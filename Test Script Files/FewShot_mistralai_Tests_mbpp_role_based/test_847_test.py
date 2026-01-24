import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_list_with_none(self):
        self.assertEqual(lcopy([None]), [None])

    def test_list_with_string(self):
        self.assertEqual(lcopy(["hello"]), ["hello"])

    def test_list_with_mixed_types(self):
        self.assertEqual(lcopy([1, "hello", None]), [1, "hello", None])
