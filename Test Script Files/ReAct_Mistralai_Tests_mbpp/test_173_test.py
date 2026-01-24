import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_splchar(''), '')

    def test_single_char(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(remove_splchar(char), char)

    def test_single_word(self):
        for word in ['apple', 'banana', 'cherry', 'orange', 'grape']:
            self.assertEqual(remove_splchar(word), word)

    def test_multiple_words(self):
        for sentence in ['apple banana cherry orange grape',
                          'Apple Banana Cherry Orange Grape',
                          'Apple Banana Cherry Orange Grape!',
                          'Apple Banana Cherry Orange Grape.']:
            self.assertEqual(remove_splchar(sentence), sentence.replace(' ', '').lower())

    def test_punctuation(self):
        for sentence in ['apple. banana, cherry; orange! grape@',
                          'apple.banana, cherry;orange!grape@',
                          'apple.banana, cherry;orange!grape@#$%^&*()_+-=[]{}|;:'\
                          ' Apple.Banana, Cherry;Orange!Grape@',
                          ' Apple.Banana, Cherry;Orange!Grape@#$%^&*()_+-=[]{}|;:']:
            self.assertEqual(remove_splchar(sentence), sentence.replace(' ', '').replace('.', '').replace(',', '').replace(';', '').replace('!', '').replace('@', '').lower())

    def test_special_characters(self):
        for sentence in ['apple_banana-cherry+orange@grape#',
                          'apple_banana-cherry+orange@grape#',
                          'apple_banana-cherry+orange@grape#$%^&*()_+-=[]{}|;:']:
            self.assertEqual(remove_splchar(sentence), sentence.replace(' ', '').replace('_', '').replace('-', '').replace('+', '').replace('@', '').replace('#', '').lower())

    def test_whitespace_only(self):
        self.assertEqual(remove_splchar('   '), '')

    def test_empty_list(self):
        self.assertEqual(remove_splchar([]), [])

    def test_single_element_list(self):
        for element in ['apple', 'banana', 'cherry', 'orange', 'grape']:
            self.assertEqual(remove_splchar([element]), [element])

    def test_multiple_elements_list(self):
        for elements in [['apple', 'banana', 'cherry', 'orange', 'grape'],
                          ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape'],
                          ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape!'],
                          ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape.']]:
            self.assertEqual(remove_splchar(elements), [elements[0].lower() for element in elements])
