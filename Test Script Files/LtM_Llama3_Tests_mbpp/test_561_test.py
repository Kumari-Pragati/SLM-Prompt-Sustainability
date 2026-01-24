import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_simple_assignment(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 2), ('c', 3)]), {'a': [1], 'b': [2], 'c': [3], 1: [1, 2, 3]})

    def test_empty_input(self):
        self.assertEqual(assign_elements([]), {})

    def test_single_element_assignment(self):
        self.assertEqual(assign_elements([('a', 1)]), {'a': [1], 1: [1]})

    def test_duplicate_values(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 1), ('c', 2)]), {'a': [1], 'b': [1], 'c': [2], 1: [1, 1], 2: [2]})

    def test_key_value_assignment(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 2), ('c', 3), ('d', 1)]), {'a': [1], 'b': [2], 'c': [3], 'd': [1], 1: [1, 1], 2: [2], 3: [3]})
