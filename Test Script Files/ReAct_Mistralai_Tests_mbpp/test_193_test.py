import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(remove_tuple(()), tuple)
        self.assertEqual(remove_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertIsInstance(remove_tuple((1,)), tuple)
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(remove_tuple((1, 2, 3)), tuple)
        self.assertEqual(remove_tuple((1, 2, 3)), (1, 2, 3))

    def test_duplicate_elements_tuple(self):
        self.assertIsInstance(remove_tuple((1, 1, 2, 3)), tuple)
        self.assertEqual(remove_tuple((1, 1, 2, 3)), (1, 2, 3))

    def test_mixed_types_tuple(self):
        with self.assertRaises(TypeError):
            remove_tuple((1, 'a', [1, 2, 3]))

    def test_none_type_tuple(self):
        with self.assertRaises(TypeError):
            remove_tuple((None,))

    def test_list_as_input(self):
        with self.assertRaises(TypeError):
            remove_tuple([1, 2, 3])
