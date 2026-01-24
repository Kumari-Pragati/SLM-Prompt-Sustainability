import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(remove_elements([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])
        self.assertListEqual(remove_elements(["a", "b", "c", "d", "e"], ["b", "d"]), ["a", "c", "e"])

    def test_edge_case_empty_lists(self):
        self.assertListEqual(remove_elements([], []), [])
        self.assertListEqual(remove_elements([1], []), [1])
        self.assertListEqual(remove_elements([], [1]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(remove_elements([1], [1]), [])
        self.assertListEqual(remove_elements([1], []), [1])

    def test_edge_case_single_match(self):
        self.assertListEqual(remove_elements([1, 2], [1]), [2])
        self.assertListEqual(remove_elements(["a", "b"], ["a"]), ["b"])

    def test_edge_case_reversed_lists(self):
        self.assertListEqual(remove_elements([1, 2], [2, 1]), [])
        self.assertListEqual(remove_elements(["a", "b"], ["b", "a"]), [])

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, remove_elements, (1, 2, 3), [1, 2])
        self.assertRaises(TypeError, remove_elements, [1, 2], (1, 2))
        self.assertRaises(TypeError, remove_elements, "1, 2", [1, 2])
        self.assertRaises(TypeError, remove_elements, [1, 2], "1, 2")
