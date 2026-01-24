import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))

    def test_false(self):
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_single_match(self):
        self.assertTrue(check_element((1, 2, 3), [1]))

    def test_multiple_matches(self):
        self.assertTrue(check_element((1, 2, 3, 4), [1, 2]))

    def test_no_matches(self):
        self.assertFalse(check_element((1, 2, 3), []))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            check_element(None, [1, 2, 3])

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            check_element("test", [1, 2, 3])
