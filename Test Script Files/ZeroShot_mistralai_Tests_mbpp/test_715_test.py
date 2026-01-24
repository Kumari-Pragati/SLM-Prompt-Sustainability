import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsInstance(str_to_tuple(''), tuple)
        self.assertEqual(str_to_tuple(''), ())

    def test_single_element(self):
        self.assertIsInstance(str_to_tuple('1'), tuple)
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_multiple_elements(self):
        self.assertIsInstance(str_to_tuple('1, 2, 3'), tuple)
        self.assertEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))

    def test_multiple_elements_with_spaces(self):
        self.assertIsInstance(str_to_tuple(' 1 , 2 , 3 '), tuple)
        self.assertEqual(str_to_tuple(' 1 , 2 , 3 '), (1, 2, 3))

    def test_multiple_elements_with_commas_only(self):
        self.assertIsInstance(str_to_tuple(',,,'), tuple)
        self.assertEqual(str_to_tuple(',,,'), ())

    def test_invalid_input(self):
        self.assertRaises(ValueError, str_to_tuple, 'a,1,b')
        self.assertRaises(ValueError, str_to_tuple, '1,a,2')
        self.assertRaises(ValueError, str_to_tuple, '1,2,a')
