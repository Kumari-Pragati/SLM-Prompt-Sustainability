import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(assign_elements([]), {})

    def test_single_element(self):
        self.assertDictEqual(assign_elements([(1, 1)]), {1: [1]})

    def test_multiple_elements(self):
        self.assertDictEqual(assign_elements([(1, 1), (2, 1), (1, 2)]), {1: [2, 1], 2: [1]})

    def test_duplicate_keys(self):
        self.assertDictEqual(assign_elements([(1, 1), (1, 2), (1, 1)]), {1: [2, 1]})

    def test_duplicate_values(self):
        self.assertDictEqual(assign_elements([(1, 1), (2, 1), (1, 1), (2, 2)]), {1: [1, 2], 2: [1, 2]})
