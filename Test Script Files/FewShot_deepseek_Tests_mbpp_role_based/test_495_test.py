import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_lowercase('HelloWorld'), 'HW')

    def test_edge_condition(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_lowercase('a'), '')
        self.assertEqual(remove_lowercase('123'), '123')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
