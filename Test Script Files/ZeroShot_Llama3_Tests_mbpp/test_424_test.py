import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_extract_rear(self):
        self.assertEqual(extract_rear((("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i"))), ["c", "f", "i"])
        self.assertEqual(extract_rear((("j", "k", "l"), ("m", "n", "o"), ("p", "q", "r"))), ["l", "o", "r"])
        self.assertEqual(extract_rear((("s", "t", "u"), ("v", "w", "x"), ("y", "z", "a"))), ["u", "x", "a"])

    def test_extract_rear_empty(self):
        self.assertEqual(extract_rear(()), [])

    def test_extract_rear_single(self):
        self.assertEqual(extract_rear((("a", "b", "c"))), ["c"])

    def test_extract_rear_single_empty(self):
        self.assertEqual(extract_rear(()), [])
