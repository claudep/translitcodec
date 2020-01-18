"""Very basic codec tests.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.

"""
import codecs
import translitcodec
from unittest import TestCase


class CodecTests(TestCase):
    data = '£ ☹ wøóf méåw'

    def test_default(self):
        assert codecs.encode(self.data, 'transliterate') == 'GBP :-( woof meaaw'

    def test_translit_long(self):
        assert codecs.encode(self.data, 'translit/long') == 'GBP :-( woof meaaw'

    def test_translit_short(self):
        assert codecs.encode(self.data, 'translit/short') == 'GBP :-( woof meaw'

    def test_translit_one(self):
        assert codecs.encode(self.data, 'translit/one') == '\u00a3 \u2639 woof meaw'

    def test_translit_long_ascii(self):
        assert self.data.encode('translit/long/ascii') == b'GBP :-( woof meaaw'

    def test_translit_short_ascii(self):
        assert self.data.encode('translit/short/ascii') == b'GBP :-( woof meaw'

    def test_translit_one_ascii(self):
        try:
            codecs.encode(self.data, 'translit/one/ascii')
            assert False
        except UnicodeEncodeError:
            assert True

        assert codecs.encode(self.data, 'translit/one/ascii', 'replace') == b'? ? woof meaw'

    def test_ascii_level_characters_remain(self):
        assert codecs.encode("'", 'translit/long') == "'"

    def test_zero_width_space(self):
        try:
            char = codecs.encode('\u200b', 'translit/long')
            assert char == ''
        except TypeError:
            assert False


class AlphabetTests(TestCase):
    def test_vietnamese(self):
        alphabet_upper = 'AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY'
        alphabet_lower = 'aăâbcdđeêghiklmnoôơpqrstuưvxy'
        self.assertEqual(
            codecs.encode(alphabet_upper, 'transliterate'),
            'AAABCDDEEGHIKLMNOOOPQRSTUUVXY'
        )
        self.assertEqual(
            codecs.encode(alphabet_lower, 'transliterate'),
            'aaabcddeeghiklmnooopqrstuuvxy'
        )
