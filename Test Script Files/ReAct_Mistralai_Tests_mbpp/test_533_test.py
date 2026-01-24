import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_datatype([], int), [])

    def test_single_element(self):
        self.assertListEqual(remove_datatype([1], int), [])
        self.assertListEqual(remove_datatype([1.0], float), [])
        self.assertListEqual(remove_datatype(["str"], str), [])

    def test_multiple_elements(self):
        self.assertListEqual(remove_datatype([1, 2, 3], int), [2, 3])
        self.assertListEqual(remove_datatype([1.0, 2.0, 3.0], float), [1, 3])
        self.assertListEqual(remove_datatype(["str1", "str2", "num"], str), ["num"])

    def test_mixed_data_types(self):
        self.assertListEqual(remove_datatype([1, 1.0, "str", [1, 2, 3]], int), [1.0, "str", [1, 2, 3]])
        self.assertListEqual(remove_datatype(["str", 1, 1.0, [1, 2, 3]], str), [1, 1.0, [1, 2, 3]])

    def test_invalid_datatype(self):
        with self.assertRaises(TypeError):
            remove_datatype([1, 2, 3], "str")
