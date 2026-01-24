import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_element_list(self):
        self.assertFalse(empty_dit([1]))

    def test_multiple_elements_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_empty_string(self):
        self.assertTrue(empty_dit([]))

    def test_single_element_string(self):
        self.assertFalse(empty_dit(["a"]))

    def test_multiple_elements_string(self):
        self.assertFalse(empty_dit(["a", "b", "c"]))

    def test_empty_set(self):
        self.assertTrue(empty_dit({}))

    def test_single_element_set(self):
        self.assertFalse(empty_dit({1}))

    def test_multiple_elements_set(self):
        self.assertFalse(empty_dit({1, 2, 3}))

    def test_empty_tuple(self):
        self.assertTrue(empty_dit(()))

    def test_single_element_tuple(self):
        self.assertFalse(empty_dit((1,)))

    def test_multiple_elements_tuple(self):
        self.assertFalse(empty_dit((1, 2, 3)))
