# -*- coding: utf-8 -*-
"""Very basic codec tests.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.

"""
import codecs
import translitcodec


data = u'£ ☹ wøóf méåw'

def test_default():
    assert codecs.encode(data, 'transliterate') == u'GBP :-( woof meaaw'

def test_translit_long():
    assert codecs.encode(data, 'translit/long') == u'GBP :-( woof meaaw'

def test_translit_short():
    assert codecs.encode(data, 'translit/short') == u'GBP :-( woof meaw'

def test_translit_one():
    assert codecs.encode(data, 'translit/one') == u'\u00a3 \u2639 woof meaw'

def test_translit_long_ascii():
    data.encode('translit/long/ascii') == b'GBP :-( woof meaaw'

def test_translit_short_ascii():
    data.encode('translit/short/ascii') == b'GBP :-( woof meaw'

def test_translit_one_ascii():
    try:
        codecs.encode(data, 'translit/one/ascii')
        assert False
    except UnicodeEncodeError:
        assert True

    assert codecs.encode(data, 'translit/one/ascii', 'replace') == b'? ? woof meaw'

def test_ascii_level_characters_remain():
    assert codecs.encode(u"'", 'translit/long') == u"'"

def test_zero_width_space():
    try:
        char = codecs.encode(u'\u200b', 'translit/long')
        assert char == u''
    except TypeError:
        assert False
