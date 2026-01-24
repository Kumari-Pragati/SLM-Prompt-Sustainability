import unittest
from mbpp_115_code import empty_dit

class TestEmptyDitFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_element_list(self):
        self.assertFalse(empty_dit([1]))

    def test_multiple_elements_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))

    def test_list_with_empty_strings(self):
        self.assertFalse(empty_dit([ '', 'a', 'b' ]))

    def test_list_with_none(self):
        self.assertFalse(empty_dit([None, 'a', 'b']))

    def test_list_with_falsy_values(self):
        self.assertTrue(empty_dit([False, None, 0, '', []]))
