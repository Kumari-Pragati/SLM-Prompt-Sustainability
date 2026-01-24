import unittest
from mbpp_533_code import remove_datatype

class TestRemoveDatatype(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4, 5), int), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(remove_datatype((1, 2, 'a', 4, 5), int), [1, 2, 4, 5])

    def test_edge_case2(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4, 'a'), int), [1, 2, 3, 4])

    def test_edge_case3(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4, 5), str), [])

    def test_edge_case4(self):
        self.assertEqual(remove_datatype((1, 2, 3, 4, 5), float), [1, 2, 3, 4, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_datatype((1, 2, 3, 4, 5), 'invalid_type')
