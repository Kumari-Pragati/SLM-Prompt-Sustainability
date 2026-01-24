import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_max_length_list(self):
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry']), (9, 'banana'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date']), (6, 'apple'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry']), (13, 'elderberry'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']), (4, 'fig'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']), (7, 'grape'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']), (11, 'honeydew'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream']), (13, 'ice cream'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit']), (13, 'jackfruit'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi']), (8, 'kiwi'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon']), (6, 'lemon'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango']), (6,'mango'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine']), (9, 'nectarine'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange']), (7, 'orange'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple']), (12, 'pineapple'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince']), (7, 'quince'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry']), (10, 'raspberry'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry','strawberry']), (13,'strawberry'))
        self.assertEqual(max_length_list(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple',