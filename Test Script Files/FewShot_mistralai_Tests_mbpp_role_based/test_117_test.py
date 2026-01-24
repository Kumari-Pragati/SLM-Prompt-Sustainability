import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(list_to_float([]), "[]")

    def test_single_element_list(self):
        self.assertEqual(list_to_float([(1,)]), "[('1', 1.0)]")

    def test_mixed_list(self):
        self.assertEqual(list_to_float([('a', 1.0), ('b', 2.0), ('c', 3.0)]), "[('a', 'a'), ('1.0', 1.0), ('2.0', 2.0), ('3.0', 3.0)]")

    def test_all_strings_list(self):
        self.assertEqual(list_to_float([('a',), ('b',), ('c',)]), "[('a', 'a'), ('b', 'b'), ('c', 'c')]")

    def test_all_floats_list(self):
        self.assertEqual(list_to_float([(1.0,), (2.0,), (3.0,)]), "[('', 1.0), ('', 2.0), ('', 3.0)]")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            list_to_float([(1, 'a'), ('b', 2, 'c')])
