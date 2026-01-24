import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(assign_elements([('a', 1), ('a', 2), ('b', 3), ('b', 4)]), {'a': [1, 2], 'b': [3, 4]})

    def test_empty_input(self):
        self.assertDictEqual(assign_elements([]), {})

    def test_single_element_input(self):
        self.assertDictEqual(assign_elements([('a', 'a')]), {'a': ['a']})

    def test_duplicate_key_input(self):
        self.assertDictEqual(assign_elements([('a', 1), ('a', 1), ('b', 2)]), {'a': [1], 'b': [2]})

    def test_duplicate_value_input(self):
        self.assertDictEqual(assign_elements([('a', 1), ('a', 1), ('b', 2), ('b', 2)]), {'a': [1], 'b': [2, 2]})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            assign_elements([(1, 'a'), ('a', 1)])
