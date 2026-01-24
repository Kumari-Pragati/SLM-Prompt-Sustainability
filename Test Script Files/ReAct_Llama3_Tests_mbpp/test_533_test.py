import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_case(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 'a', 2.5, 'b', 3])

    def test_edge_case(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b'])

    def test_edge_case2(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.5, 3])

    def test_edge_case3(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case4(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b'])

    def test_edge_case5(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.5, 3])

    def test_edge_case6(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case7(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b'])

    def test_edge_case8(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.5, 3])

    def test_edge_case9(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case10(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b'])

    def test_edge_case11(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.5, 3])

    def test_edge_case12(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case13(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = str
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, ['a', 'b'])

    def test_edge_case14(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = float
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2.5, 3])

    def test_edge_case15(self):
        test_tuple = (1, 'a', 2.5, 'b', 3)
        data_type = int
        result = remove_datatype(test_tuple, data_type)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case16(self):
        test_tuple = (1, 'a', 2.5, '