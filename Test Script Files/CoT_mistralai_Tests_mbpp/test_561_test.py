import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertDictEqual(assign_elements([('a', 'a'),]), {'a': ['a']})

    def test_multiple_elements(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'a'), ('c', 'b'), ('a', 'c')]), {'a': ['a', 'c'], 'b': ['b'], 'c': []})

    def test_duplicate_keys(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('a', 'b'), ('a', 'c')]), {'a': ['a', 'b', 'c']})

    def test_duplicate_values(self):
        self.assertDictEqual(assign_elements([('a', 'a'), ('b', 'a'), ('c', 'a')]), {'a': ['a', 'b', 'c'], 'b': [], 'c': []})

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            assign_elements([(1, 'a'),])

    def test_invalid_input_2(self:
