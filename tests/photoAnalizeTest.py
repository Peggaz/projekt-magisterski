import unittest

from photo_analize import PhotoAnalize


class TestPhotoAnalize(unittest.TestCase):
    def setUp(self):
        self.pa = PhotoAnalize('wig20.png')

    def test_makeAndGetFotoMap(self):
        expected_length = 643
        foto_map = self.pa.makeAndGetFotoMap()
        self.assertIsInstance(foto_map, list)
        self.assertEqual(len(foto_map), expected_length)

    def test_valid_map(self):
        invalid_map = [(1, 1), (3, 2), (2, 3)]
        valid_map = [(1, 1), (2, 2), (3, 3)]
        self.assertFalse(self.pa.validMap(invalid_map))
        self.assertTrue(self.pa.validMap(valid_map))

    def test_is_in_range(self):
        self.assertFalse(self.pa.isInRange(3, (1, 2)))
        self.assertTrue(self.pa.isInRange(2, (1, 3)))

    def test_get_word_in_grammar(self):
        self.assertEqual(self.pa.getTermInGrammar(2), 'x')
        self.assertEqual(self.pa.getTermInGrammar(5), 'X')

    def test_makeGrammar(self):
        grammar = self.pa.makeGrammar()
        self.assertIsInstance(grammar, str)
        self.assertEqual(grammar, expected_grammar)

if __name__ == '__main__':
    unittest.main()
