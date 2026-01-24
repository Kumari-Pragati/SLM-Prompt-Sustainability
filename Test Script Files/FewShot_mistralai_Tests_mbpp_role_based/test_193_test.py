import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_remove_single_element_tuple(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_remove_duplicate_elements_tuple(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3)), (1, 2, 3))

    def test_empty_tuple(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_single_element_list_converted_to_tuple(self):
        self.assertEqual(remove_tuple([1]), (1,))

    def test_tuple_with_non_hashable_element(self):
        with self.assertRaises(TypeError):
            remove_tuple((1, "list"))
