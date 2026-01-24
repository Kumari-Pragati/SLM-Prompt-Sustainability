import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertDictEqual(assign_elements([(1, 2), (1, 3), (2, 3)]), {'1': [2, 3], '2': [3]})

    def test_empty_list(self):
        self.assertDictEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertDictEqual(assign_elements([(1, 1)]), {'1': [1]})

    def test_edge_case_key_not_in_list(self):
        self.assertDictEqual(assign_elements([(1, 2), (2, 3)]), {'1': [2], '2': [3]})

    def test_edge_case_value_not_in_list(self):
        self.assertDictEqual(assign_elements([(1, 2), (1, 3)]), {'1': [2, 3]})
