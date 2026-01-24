import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_multiple_element_list(self):
        self.assertEqual(Extract([[1, 2], [3, 4], [5, 6]]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, "hello", 3.14])
