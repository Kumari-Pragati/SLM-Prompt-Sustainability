import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(list_to_float([]), '[]')

    def test_single_element(self):
        self.assertEqual(list_to_float([['1.0']]), '[(\'1.0\', \'1.0\')]')

    def test_multiple_elements(self):
        self.assertEqual(list_to_float([['1.0', '2.0'], ['3.0', '4.0']]), '[(\'1.0\', \'2.0\'), (\'3.0\', \'4.0\')]')

    def test_mixed_types(self):
        self.assertEqual(list_to_float([['1.0', 'hello'], ['3.0', '4.0']]), '[(\'1.0\', \'hello\'), (\'3.0\', \'4.0\')]')

    def test_empty_sublist(self):
        self.assertEqual(list_to_float([['1.0', '2.0'], ['', '4.0']]), '[(\'1.0\', \'2.0\'), (\'\', \'4.0\')]')

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            list_to_float([['1.0', 'hello'], ['3.0', '4.0']])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            list_to_float('test')
