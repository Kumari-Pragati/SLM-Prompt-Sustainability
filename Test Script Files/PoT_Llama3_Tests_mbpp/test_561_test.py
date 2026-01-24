import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 2), ('c', 3)]), 
                         {'a': [1], 'b': [2], 'c': [3], 1: [1], 2: [2], 3: [3]})

    def test_edge_case_empty_list(self):
        self.assertEqual(assign_elements([]), {})

    def test_edge_case_single_element(self):
        self.assertEqual(assign_elements([('a', 1)]), {'a': [1], 1: [1]})

    def test_edge_case_duplicate_keys(self):
        self.assertEqual(assign_elements([('a', 1), ('a', 2)]), 
                         {'a': [1, 2], 1: [1], 2: [2]})

    def test_edge_case_duplicate_values(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 1)]), 
                         {'a': [1], 'b': [1], 1: [1]})

    def test_edge_case_key_value_pair_order(self):
        self.assertEqual(assign_elements([('a', 1), ('b', 2), ('c', 3)]), 
                         {'a': [1], 'b': [2], 'c': [3], 1: [1], 2: [2], 3: [3]})

    def test_edge_case_key_value_pair_order_reversed(self):
        self.assertEqual(assign_elements([('c', 3), ('b', 2), ('a', 1)]), 
                         {'a': [1], 'b': [2], 'c': [3], 1: [1], 2: [2], 3: [3]})
