import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_tuple([(1, 2, 3), (4, None, 6), (7, 8, None)]), "'[(1, 2, 3), (4, 6, 6)]'")

    def test_empty_list(self):
        self.assertEqual(remove_tuple([]), "'[]'")

    def test_single_element_list(self):
        self.assertEqual(remove_tuple([(1,)]), "'[(1,)]'")

    def test_all_none_tuple(self):
        self.assertEqual(remove_tuple([(None, None, None)]), "'[]'")

    def test_all_ints(self):
        self.assertEqual(remove_tuple([(1, 2, 3), (4, 5, 6)]), "'[(1, 2, 3)]'")

    def test_all_floats(self):
        self.assertEqual(remove_tuple([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]), "'[(1.0, 2.0, 3.0)]'")

    def test_mixed_types(self):
        self.assertEqual(remove_tuple([(1, 2, 3), (4, 'str', 6), (7, 8, None)]), "'[(1, 2, 3), (4, 'str', 6)]'")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_tuple(123)
