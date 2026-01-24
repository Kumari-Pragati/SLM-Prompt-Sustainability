import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_datatype((1, 2.0, '3', [4]), int), (2.0, '3', [4]))
        self.assertEqual(remove_datatype(('1', 2, 3.0, [4]), str), (1, 2, 3.0, [4]))
        self.assertEqual(remove_datatype((1, 2, 3, [4.0]), float), (1, 2, 3, [4.0]))
        self.assertEqual(remove_datatype((1, 2, 3, [4]), list), (1, 2, 3))

    def test_edge_case(self):
        self.assertEqual(remove_datatype((0, 2.0, '3', [4]), int), (2.0, '3', [4]))
        self.assertEqual(remove_datatype((1, 0.0, '3', [4]), int), (1, '3', [4]))
        self.assertEqual(remove_datatype((1, 2, 0, [4]), int), (1, 2, [4]))
        self.assertEqual(remove_datatype((1, 2, 3, 4), int), [1, 2, 3])
        self.assertEqual(remove_datatype((1, 2, 3, 4), float), (1, 2, 3, 4))
        self.assertEqual(remove_datatype((1, 2, 3, 4), str), (1, 2, 3, 4))
        self.assertEqual(remove_datatype((1, 2, 3, 4), list), (1, 2, 3))

    def test_corner_case(self):
        self.assertEqual(remove_datatype((1, 2, 3, (4,)), int), (1, 2, 3))
        self.assertEqual(remove_datatype((1, 2, 3, (4,)), float), (1, 2, 3))
        self.assertEqual(remove_datatype((1, 2, 3, (4,)), str), (1, 2, 3))
        self.assertEqual(remove_datatype((1, 2, 3, (4,)), list), (1, 2, 3))
