import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_find_max_length(self):
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry']), 7)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date']), 7)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry']), 12)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']), 12)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']), 12)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']), 13)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream']), 14)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit']), 15)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi']), 16)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon']), 17)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango']), 18)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine']), 19)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange']), 20)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple']), 21)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince']), 22)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry']), 23)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry','strawberry']), 24)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry','strawberry', 'tangerine']), 25)
        self.assertEqual(Find_Max_Length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'gr