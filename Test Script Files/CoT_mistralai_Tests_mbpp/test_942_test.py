import unittest
from942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(check_element((), []))

    def test_empty_tuple(self):
        self.assertFalse(check_element((), (1, 2, 3)))

    def test_single_element_tuple(self):
        self.assertTrue(check_element((1,), [1]))
        self.assertFalse(check_element((1,), [2]))

    def test_multiple_elements_tuple(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_list_of_tuples(self):
        self.assertTrue(check_element((1,), [(1,), (2,), (3,)]))
        self.assertFalse(check_element((1,), [(2,), (3,), (4,)]))

    def test_list_of_different_types(self):
        self.assertRaises(TypeError, check_element, (1, 'a'), [1, 2, 3.14])

    def test_none_type(self):
        self.assertRaises(TypeError, check_element, (1, None), [1, 2, 3])
