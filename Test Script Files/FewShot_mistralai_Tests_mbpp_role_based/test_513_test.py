import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(add_str(((1, 2), (3, 4)), 'K'), ['1', '2', '3', '4', 'K'])

    def test_single_element_list(self):
        self.assertListEqual(add_str(((1,),), 'K'), ['1', 'K'])

    def test_empty_list(self):
        self.assertListEqual(add_str(((1,),), ''), [])

    def test_empty_tuple(self):
        self.assertListEqual(add_str(()), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            add_str('a', 'b')
