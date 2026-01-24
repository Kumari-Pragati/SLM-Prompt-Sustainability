import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove([]), [])

    def test_single_element_list(self):
        self.assertListEqual(remove(['A']), ['A'])
        self.assertListEqual(remove(['1']), [])
        self.assertListEqual(remove(['A1']), ['A'])

    def test_multiple_elements_list(self):
        self.assertListEqual(remove(['A', '1', 'B']), ['A', 'B'])
        self.assertListEqual(remove(['1', 'A', '1']), [])
        self.assertListEqual(remove(['A1B', '1A2', 'A1B1']), ['AB', 'A2'])

    def test_string_list(self):
        self.assertListEqual(remove(['Hello', 'World', '123']), ['Hello', 'World'])
        self.assertListEqual(remove(['1Hello', 'World1', '123World']), ['Hello', 'World'])
        self.assertListEqual(remove(['1HelloWorld', 'World123', '123HelloWorld1']), ['HelloWorld', 'World123'])

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove, 123)
        self.assertRaises(TypeError, remove, (1, 2, 3))
        self.assertRaises(TypeError, remove, {'key': 'value'})
