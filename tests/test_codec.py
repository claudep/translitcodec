# -*- coding: utf-8 -*-
"""Very basic codec tests.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.

"""
import translitcodec


data = u'£ ☹ wøóf méåw'

def test_default():
    assert data.encode('transliterate') == u'GBP :-( woof meaaw'

def test_translit_long():
    assert data.encode('translit/long') == u'GBP :-( woof meaaw'

def test_translit_short():
    assert data.encode('translit/short') == u'GBP :-( woof meaw'

def test_translit_one():
    assert data.encode('translit/one') == u'\u00a3 \u2639 woof meaw'

def test_translit_long_ascii():
    assert data.encode('translit/long/ascii') == 'GBP :-( woof meaaw'

def test_translit_short_ascii():
    assert data.encode('translit/short/ascii') == u'GBP :-( woof meaw'

def test_translit_one_ascii():
    try:
        data.encode('translit/one/ascii')
        assert False
    except UnicodeEncodeError:
        assert True

    assert data.encode('translit/one/ascii', 'replace') == '? ? woof meaw'

def test_ascii_level_characters_remain():
    assert u"'".encode('translit/long') == u"'"

def test_zero_width_space():
    try:
        char = u'\u200b'.encode('translit/long')
        assert char == u''
    except TypeError:
        assert False
