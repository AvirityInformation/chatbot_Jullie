from unittest import TestCase, main

from common.word_format.word_formatter import WordFormatter


class TestWordFormatter(TestCase):
    def test_wtok2str(self):
        test_patterns = [
            (('i', 'am', 'sad'), "i am sad."),
            (('thank', 'you'), "thank you."),
            (None, None),
            ([], [])
        ]

        for x, y in test_patterns:
            with self.subTest(x=x):
                result = WordFormatter.wtok2str(x)
                self.assertEqual(y, result)

    def test_wtoks2str(self):
        test_patterns = [
            ([['i', 'am', 'sad'], ['thank', 'you']], "i am sad. thank you."),
            (None, None),
            ([], [])
        ]

        for x, y in test_patterns:
            with self.subTest(x=x):
                result = WordFormatter.wtoks2str(x)
                self.assertEqual(y, result)


if __name__ == "__main__":
    main()
