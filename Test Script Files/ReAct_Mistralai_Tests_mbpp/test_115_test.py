import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_element_list(self):
        self.assertFalse(empty_dit([1]))
        self.assertFalse(empty_dit([0]))
        self.assertFalse(empty_dit([False]])
        self.assertFalse(empty_dit([None]])

    def test_multiple_elements_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))
        self.assertFalse(empty_dit([0, 0, 0]))
        self.assertFalse(empty_dit([False, False, False]))
        self.assertFalse(empty_dit([None, None, None]))

    def test_list_with_empty_tuple_or_list(self):
        self.assertFalse(empty_dit([(), ()]))
        self.assertFalse(empty_dit([[], []]))
        self.assertFalse(empty_dit([(1,), (1,)]))
        self.assertFalse(empty_dit([[1], [1]]))

    def test_list_with_empty_dict(self):
        self.assertFalse(empty_dit([{}, {}]))

    def test_list_with_empty_set(self):
        self.assertFalse(empty_dit([set(), set()]))
