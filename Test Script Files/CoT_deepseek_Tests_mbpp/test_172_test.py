import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sdt is good'), 1)
        self.assertEqual(count_occurance('sdt is good, sdt is bad'), 2)

    def test_edge_cases(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('not sdt'), 0)
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sdt, sdt, sdt'), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_occurance(123)
        with self.assertRaises(TypeError):
            count_occurance(['sdt', 'sdt', 'sdt'])
