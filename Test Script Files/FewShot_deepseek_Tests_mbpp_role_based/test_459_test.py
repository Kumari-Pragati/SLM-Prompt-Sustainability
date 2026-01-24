import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')

    def test_edge_condition(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_uppercase('A'), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)
