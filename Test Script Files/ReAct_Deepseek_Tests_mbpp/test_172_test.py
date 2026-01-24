import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sdt is good'), 1)
        self.assertEqual(count_occurance('this is a test string'), 1)

    def test_edge_cases(self):
        self.assertEqual(count_occurance(''), 0)
        self.assertEqual(count_occurance('s'), 0)
        self.assertEqual(count_occurance('st'), 0)
        self.assertEqual(count_occurance('sd'), 0)
        self.assertEqual(count_occurance('sdt'), 1)
        self.assertEqual(count_occurance('sdt '), 0)
        self.assertEqual(count_occurance(' sdt'), 0)
        self.assertEqual(count_occurance('sdt is good'), 1)
        self.assertEqual(count_occurance('this is a test string'), 1)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, this test case is redundant.
        pass
