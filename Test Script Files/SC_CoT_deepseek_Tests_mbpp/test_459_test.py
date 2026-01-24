import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_edge_case_all_uppercase(self):
        self.assertEqual(remove_uppercase('HELLO'), 'ello')

    def test_corner_case_mixed_case(self):
        self.assertEqual(remove_uppercase('hElLO'), 'ello')

    def test_corner_case_special_characters(self):
        self.assertEqual(remove_uppercase('Hello@World'), 'ello@orld')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_uppercase(12345)
