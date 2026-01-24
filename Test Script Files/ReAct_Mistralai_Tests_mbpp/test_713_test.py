import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTrue(check_valid(()))

    def test_single_element_tuple(self):
        for element in [True, False]:
            self.assertFalse(check_valid((element,)))

    def test_multiple_elements_tuple(self):
        for elements in [(True, True), (False, False), (True, False, True)]:
            self.assertTrue(check_valid(elements))

    def test_longer_tuple(self):
        for elements in [(True, True, False, True), (False, True, False, True)]:
            self.assertTrue(check_valid(elements))

    def test_none_type(self):
        self.assertRaises(TypeError, check_valid, (None,))

    def test_list_type(self):
        self.assertRaises(TypeError, check_valid, [True])
