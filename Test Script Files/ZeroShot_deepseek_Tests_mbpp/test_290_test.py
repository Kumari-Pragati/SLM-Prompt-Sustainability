import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_max_length(self):
        self.assertEqual(max_length(['abc', 'de', 'fghi']), (4, 'fghi'))
        self.assertEqual(max_length(['abc', 'de', 'fghij']), (5, 'fghij'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop']), (6, 'klmnop'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrs']), (5, 'klmnop'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrstu']), (5, 'qrstu'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrstuv']), (6, 'qrstuv'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrstuvw']), (7, 'qrstuvw'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrstuvwx']), (8, 'qrstuvwx'))
        self.assertEqual(max_length(['abc', 'de', 'fghij', 'klmnop', 'qrstuvwxy']), (9, 'qrstuvwxy'))
