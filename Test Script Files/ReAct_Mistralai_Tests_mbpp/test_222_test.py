import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTrue(check_type(()))

    def test_single_element_tuple(self):
        for element in [1, 'a', (1,), None]:
            self.assertTrue(check_type((element,)))

    def test_multiple_elements_same_type(self):
        for elements in [(1, 1), (1.0, 1.0), (str('a'), str('a')), (tuple([1]), tuple([1]))]:
            self.assertTrue(check_type(elements))

    def test_multiple_elements_different_types(self):
        for elements in [(1, 'a'), (1.0, 1), (str('a'), tuple([1]))]:
            self.assertFalse(check_type(elements))

    def test_mixed_types_same_base_type(self):
        for elements in [(1.0, 2.0), (str('a'), str('b')), (tuple([1]), tuple([2]))]:
            self.assertTrue(check_type(elements))

    def test_mixed_types_different_base_types(self):
        for elements in [(1, 'a'), (1.0, 2), (str('a'), tuple([1]))]:
            self.assertFalse(check_type(elements))

    def test_none_type(self):
        self.assertTrue(check_type((None,)))

    def test_list_type(self):
        self.assertFalse(check_type([1, 'a']))
