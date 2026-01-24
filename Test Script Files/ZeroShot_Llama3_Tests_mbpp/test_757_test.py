import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_count_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c']), '3')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd']), '6')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e']), '10')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f']), '15')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g']), '21')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']), '28')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']), '36')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']), '45')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']), '55')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']), '66')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m']), '78')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n']), '91')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o']), '105')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p']), '120')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q']), '136')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r']), '153')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s']), '171')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't']), '190')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u']), '210')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v']), '231')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', '