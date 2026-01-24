import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_min_length(self):
        self.assertEqual(min_length(['apple', 'banana', 'cherry']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry','strawberry']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iguana', 'jackfruit', 'kiwi', 'lemon','mango', 'nectarine', 'orange', 'pineapple', 'quince', 'raspberry','strawberry', 'tangerine']), (5, 'apple'))
        self.assertEqual(min_length(['apple', 'banana', 'ch