import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_occurance('sdt'), 1)

    def test_edge_case(self):
        self.assertEqual(count_occurance(''), 0)

    def test_boundary_case(self):
        self.assertEqual(count_occurance('s'*10000 + 't'*10000 + 'd'*10000), 10000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_occurance(123)

    def test_no_occurrence(self):
        self.assertEqual(count_occurance('abc'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(count_occurance('ssttdds'), 2)
