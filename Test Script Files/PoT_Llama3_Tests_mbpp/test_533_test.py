import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_datatype((1, 2, 3), int), [2, 3])

    def test_edge_case(self):
        self.assertEqual(remove_datatype((1, 2, 3), str), [1, 2, 3])

    def test_edge_case2(self):
        self.assertEqual(remove_datatype((1, 2, 3), float), [1, 2, 3])

    def test_edge_case3(self):
        self.assertEqual(remove_datatype((1, 2, 3), bool), [1, 2, 3])

    def test_edge_case4(self):
        self.assertEqual(remove_datatype((1, 2, 3), object), [1, 2, 3])

    def test_edge_case5(self):
        self.assertEqual(remove_datatype((1, 2, 3), tuple), [])

    def test_edge_case6(self):
        self.assertEqual(remove_datatype((1, 2, 3), list), [])

    def test_edge_case7(self):
        self.assertEqual(remove_datatype((1, 2, 3), dict), [])

    def test_edge_case8(self):
        self.assertEqual(remove_datatype((1, 2, 3), set), [])

    def test_edge_case9(self):
        self.assertEqual(remove_datatype((1, 2, 3), frozenset), [])

    def test_edge_case10(self):
        self.assertEqual(remove_datatype((1, 2, 3), bytes), [])

    def test_edge_case11(self):
        self.assertEqual(remove_datatype((1, 2, 3), bytearray), [])

    def test_edge_case12(self):
        self.assertEqual(remove_datatype((1, 2, 3), memoryview), [])

    def test_edge_case13(self):
        self.assertEqual(remove_datatype((1, 2, 3), slice), [])

    def test_edge_case14(self):
        self.assertEqual(remove_datatype((1, 2, 3), range), [])

    def test_edge_case15(self):
        self.assertEqual(remove_datatype((1, 2, 3), complex), [])

    def test_edge_case16(self):
        self.assertEqual(remove_datatype((1, 2, 3), ellipsis), [])

    def test_edge_case17(self):
        self.assertEqual(remove_datatype((1, 2, 3), None), [1, 2, 3])

    def test_edge_case18(self):
        self.assertEqual(remove_datatype((1, 2, 3), type(None)), [])

    def test_edge_case19(self):
        self.assertEqual(remove_datatype((1, 2, 3), type), [])

    def test_edge_case20(self):
        self.assertEqual(remove_datatype((1, 2, 3), type(None)), [])
