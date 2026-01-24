import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_multiple_elements_tuple(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3)), (1, 2, 3))

    def test_duplicates_in_tuple(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3, 3)), (1, 2, 3))

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            remove_tuple([])

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            remove_tuple("test")
