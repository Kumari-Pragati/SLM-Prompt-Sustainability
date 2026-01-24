import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(list_to_float([]), "[]")

    def test_single_element_list(self):
        self.assertEqual(list_to_float([1]), "[('', 1.0)]")
        self.assertEqual(list_to_float([str(1)]), "[('', 1.0)]")

    def test_mixed_list(self):
        self.assertEqual(list_to_float([1, 'a', 2.5, 'b', 3]), "[('a', 1.0), ('', 2.5), ('b', 3.0)]")
        self.assertEqual(list_to_float([str(1), 'a', float(2.5), 'b', str(3)]), "[('a', 1.0), ('', 2.5), ('b', 3.0)]")

    def test_all_strings_list(self):
        self.assertEqual(list_to_float(['a', 'b', 'c']), "[('a', ''), ('b', ''), ('c', '')]")

    def test_list_with_only_strings(self):
        self.assertEqual(list_to_float(['', 'a', 'b', 'c']), "[('', 'a'), ('', 'b'), ('', 'c')]")

    def test_list_with_only_floats(self):
        self.assertEqual(list_to_float([1.1, 2.2, 3.3]), "[('', 1.1), ('', 2.2), ('', 3.3)]")

    def test_list_with_non_numeric_strings(self):
        self.assertEqual(list_to_float([1, 'abc', 2, 'xyz', 3]), "[('', 1.0), ('abc', ''), ('', 2.0), ('xyz', ''), ('', 3.0)]")
