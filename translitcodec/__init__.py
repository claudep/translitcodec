"""Unicode to 8-bit charset transliteration codec.

This package contains codecs for transliterating ISO 10646 texts into
best-effort representations using smaller coded character sets (ASCII,
ISO 8859, etc.).  The translation tables used by the codecs are from
the ``transtab`` collection by Markus Kuhn.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.

"""
import codecs
import sys
import unicodedata


__version_info__ = (0, 4, 0)
__version__ = '.'.join(str(_) for _ in __version_info__)


def long_encode(input, errors='strict'):
    """Transliterate to 8 bit using as many letters as needed.

    For example, \u00e4 LATIN SMALL LETTER A WITH DIAERESIS ``ä`` will
    be replaced with ``ae``.

    """
    if not isinstance(input, str):
        input = str(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(long_table), length


def short_encode(input, errors='strict'):
    """Transliterate to 8 bit using as few letters as possible.

    For example, \u00e4 LATIN SMALL LETTER A WITH DIAERESIS ``ä`` will
    be replaced with ``a``.

    """
    if not isinstance(input, str):
        input = str(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(short_table), length


def single_encode(input, errors='strict'):
    """Transliterate to 8 bit using only single letter replacements.

    For example, \u2639 WHITE FROWNING FACE ``☹`` will be passed
    through unchanged.

    """
    if not isinstance(input, str):
        input = str(input, sys.getdefaultencoding(), errors)
    length = len(input)
    input = unicodedata.normalize('NFKC', input)
    return input.translate(single_table), length


def no_decode(input, errors='strict'):
    raise TypeError("transliterating codec does not support decode.")


def _double_encoding_factory(encoder, byte_encoder, byte_encoding):
    """Send the transliterated output to another codec."""
    def dbl_encode(input, errors='strict'):
        uni, length = encoder(input, errors)
        return byte_encoder(uni, errors)[0], length
    dbl_encode.__name__ = '%s_%s' % (encoder.__name__, byte_encoding)
    return dbl_encode


def trans_search(encoding):
    """Lookup transliterating codecs."""
    if encoding == 'transliterate':
        return codecs.CodecInfo(long_encode, no_decode)

    # translit/long/utf8
    # translit/one
    # translit/short/ascii

    if encoding.startswith('translit/'):
        parts = encoding.split('/')
        if parts[1] == 'long':
            encoder = long_encode
        elif parts[1] == 'short':
            encoder = short_encode
        elif parts[1] == 'one':
            encoder = single_encode
        else:
            return None

        if len(parts) == 2:
            pass
        elif len(parts) == 3:
            byte_enc = parts[2]
            byte_encoder = codecs.lookup(byte_enc).encode
            encoder = _double_encoding_factory(encoder, byte_encoder, byte_enc)
        else:
            return None
        return codecs.CodecInfo(encoder, no_decode)
    return None

codecs.register(trans_search)

### Code below is generated by update_table.py; do not edit.
### >

long_table = {
  160: ' ',
  161: '!',
  162: 'c',
  163: 'GBP',
  165: 'Y',
  166: '|',
  167: 'S',
  168: '"',
  169: '(c)',
  170: 'a',
  171: '<<',
  172: '-',
  173: '-',
  174: '(R)',
  175: '-',
  176: ' ',
  177: '+/-',
  178: '^2',
  179: '^3',
  180: "'",
  181: 'μ',
  182: 'P',
  183: '.',
  184: ',',
  185: '^1',
  186: 'o',
  187: '>>',
  188: ' 1/4',
  189: ' 1/2',
  190: ' 3/4',
  191: '?',
  192: 'A',
  193: 'A',
  194: 'A',
  195: 'A',
  196: 'Ae',
  197: 'Aa',
  198: 'AE',
  199: 'C',
  200: 'E',
  201: 'E',
  202: 'E',
  203: 'E',
  204: 'I',
  205: 'I',
  206: 'I',
  207: 'I',
  208: 'D',
  209: 'N',
  210: 'O',
  211: 'O',
  212: 'O',
  213: 'O',
  214: 'Oe',
  215: 'x',
  216: 'O',
  217: 'U',
  218: 'U',
  219: 'U',
  220: 'Ue',
  221: 'Y',
  222: 'Th',
  223: 'ss',
  224: 'a',
  225: 'a',
  226: 'a',
  227: 'a',
  228: 'ae',
  229: 'aa',
  230: 'ae',
  231: 'c',
  232: 'e',
  233: 'e',
  234: 'e',
  235: 'e',
  236: 'i',
  237: 'i',
  238: 'i',
  239: 'i',
  240: 'd',
  241: 'n',
  242: 'o',
  243: 'o',
  244: 'o',
  245: 'o',
  246: 'oe',
  247: ':',
  248: 'o',
  249: 'u',
  250: 'u',
  251: 'u',
  252: 'ue',
  253: 'y',
  254: 'th',
  255: 'y',
  256: 'A',
  257: 'a',
  258: 'A',
  259: 'a',
  260: 'A',
  261: 'a',
  262: 'C',
  263: 'c',
  264: 'Ch',
  265: 'ch',
  266: 'C',
  267: 'c',
  268: 'C',
  269: 'c',
  270: 'D',
  271: 'd',
  272: 'D',
  273: 'd',
  274: 'E',
  275: 'e',
  276: 'E',
  277: 'e',
  278: 'E',
  279: 'e',
  280: 'E',
  281: 'e',
  282: 'E',
  283: 'e',
  284: 'Gh',
  285: 'gh',
  286: 'G',
  287: 'g',
  288: 'G',
  289: 'g',
  290: 'G',
  291: 'g',
  292: 'Hh',
  293: 'hh',
  294: 'H',
  295: 'h',
  296: 'I',
  297: 'i',
  298: 'I',
  299: 'i',
  300: 'I',
  301: 'i',
  302: 'I',
  303: 'i',
  304: 'I',
  305: 'i',
  306: 'IJ',
  307: 'ij',
  308: 'Jh',
  309: 'jh',
  310: 'K',
  311: 'k',
  312: 'k',
  313: 'L',
  314: 'l',
  315: 'L',
  316: 'l',
  317: 'L',
  318: 'l',
  319: 'L·',
  320: 'l·',
  321: 'L',
  322: 'l',
  323: 'N',
  324: 'n',
  325: 'N',
  326: 'n',
  327: 'N',
  328: 'n',
  329: "'n",
  330: 'NG',
  331: 'ng',
  332: 'O',
  333: 'o',
  334: 'O',
  335: 'o',
  336: 'O',
  337: 'o',
  338: 'OE',
  339: 'oe',
  340: 'R',
  341: 'r',
  342: 'R',
  343: 'r',
  344: 'R',
  345: 'r',
  346: 'S',
  347: 's',
  348: 'Sh',
  349: 'sh',
  350: 'S',
  351: 's',
  352: 'S',
  353: 's',
  354: 'T',
  355: 't',
  356: 'T',
  357: 't',
  358: 'T',
  359: 't',
  360: 'U',
  361: 'u',
  362: 'U',
  363: 'u',
  364: 'U',
  365: 'u',
  366: 'U',
  367: 'u',
  368: 'U',
  369: 'u',
  370: 'U',
  371: 'u',
  372: 'W',
  373: 'w',
  374: 'Y',
  375: 'y',
  376: 'Y',
  377: 'Z',
  378: 'z',
  379: 'Z',
  380: 'z',
  381: 'Z',
  382: 'z',
  383: 's',
  402: 'f',
  416: 'O',
  417: 'o',
  431: 'U',
  432: 'u',
  536: 'Ş',
  537: 'ş',
  538: 'Ţ',
  539: 'ţ',
  697: '′',
  699: '‘',
  700: '’',
  701: '‛',
  710: '^',
  712: "'",
  713: '¯',
  716: ',',
  720: ':',
  730: '°',
  732: '~',
  733: '"',
  884: "'",
  885: ',',
  894: ';',
  7682: 'B',
  7683: 'b',
  7690: 'D',
  7691: 'd',
  7710: 'F',
  7711: 'f',
  7744: 'M',
  7745: 'm',
  7766: 'P',
  7767: 'p',
  7776: 'S',
  7777: 's',
  7786: 'T',
  7787: 't',
  7808: 'W',
  7809: 'w',
  7810: 'W',
  7811: 'w',
  7812: 'W',
  7813: 'w',
  7918: 'U',
  7919: 'u',
  7922: 'Y',
  7923: 'y',
  8192: ' ',
  8193: '  ',
  8194: ' ',
  8195: '  ',
  8196: ' ',
  8197: ' ',
  8198: ' ',
  8199: ' ',
  8200: ' ',
  8201: ' ',
  8202: '',
  8203: '',
  8204: '',
  8205: '',
  8206: '',
  8207: '',
  8208: '-',
  8209: '-',
  8210: '-',
  8211: '-',
  8212: '--',
  8213: '--',
  8214: '||',
  8215: '_',
  8216: "'",
  8217: "'",
  8218: "'",
  8219: "'",
  8220: '"',
  8221: '"',
  8222: '"',
  8223: '"',
  8224: '+',
  8225: '++',
  8226: 'o',
  8227: '>',
  8228: '.',
  8229: '..',
  8230: '...',
  8231: '-',
  8234: '',
  8235: '',
  8236: '',
  8237: '',
  8238: '',
  8239: ' ',
  8240: ' 0/00',
  8242: "'",
  8243: '"',
  8244: "'''",
  8245: '`',
  8246: '``',
  8247: '```',
  8249: '<',
  8250: '>',
  8252: '!!',
  8254: '-',
  8259: '-',
  8260: '/',
  8264: '?!',
  8265: '!?',
  8266: '7',
  8304: '^0',
  8308: '^4',
  8309: '^5',
  8310: '^6',
  8311: '^7',
  8312: '^8',
  8313: '^9',
  8314: '^+',
  8315: '^-',
  8316: '^=',
  8317: '^(',
  8318: '^)',
  8319: '^n',
  8320: '_0',
  8321: '_1',
  8322: '_2',
  8323: '_3',
  8324: '_4',
  8325: '_5',
  8326: '_6',
  8327: '_7',
  8328: '_8',
  8329: '_9',
  8330: '_+',
  8331: '_-',
  8332: '_=',
  8333: '_(',
  8334: '_)',
  8364: 'EUR',
  8448: 'a/c',
  8449: 'a/s',
  8451: '°C',
  8453: 'c/o',
  8454: 'c/u',
  8457: '°F',
  8467: 'l',
  8470: 'Nº',
  8471: '(P)',
  8480: '[SM]',
  8481: 'TEL',
  8482: '[TM]',
  8486: 'Ω',
  8490: 'K',
  8491: 'Å',
  8494: 'e',
  8531: ' 1/3',
  8532: ' 2/3',
  8533: ' 1/5',
  8534: ' 2/5',
  8535: ' 3/5',
  8536: ' 4/5',
  8537: ' 1/6',
  8538: ' 5/6',
  8539: ' 1/8',
  8540: ' 3/8',
  8541: ' 5/8',
  8542: ' 7/8',
  8543: ' 1/',
  8544: 'I',
  8545: 'II',
  8546: 'III',
  8547: 'IV',
  8548: 'V',
  8549: 'VI',
  8550: 'VII',
  8551: 'VIII',
  8552: 'IX',
  8553: 'X',
  8554: 'XI',
  8555: 'XII',
  8556: 'L',
  8557: 'C',
  8558: 'D',
  8559: 'M',
  8560: 'i',
  8561: 'ii',
  8562: 'iii',
  8563: 'iv',
  8564: 'v',
  8565: 'vi',
  8566: 'vii',
  8567: 'viii',
  8568: 'ix',
  8569: 'x',
  8570: 'xi',
  8571: 'xii',
  8572: 'l',
  8573: 'c',
  8574: 'd',
  8575: 'm',
  8592: '<-',
  8593: '^',
  8594: '->',
  8595: 'v',
  8596: '<->',
  8656: '<=',
  8658: '=>',
  8660: '<=>',
  8722: '–',
  8725: '/',
  8726: '\\',
  8727: '*',
  8728: 'o',
  8729: '·',
  8734: 'inf',
  8739: '|',
  8741: '||',
  8758: ':',
  8764: '~',
  8800: '/=',
  8801: '=',
  8804: '<=',
  8805: '>=',
  8810: '<<',
  8811: '>>',
  8853: '(+)',
  8854: '(-)',
  8855: '(x)',
  8856: '(/)',
  8866: '|-',
  8867: '-|',
  8870: '|-',
  8871: '|=',
  8872: '|=',
  8873: '||-',
  8901: '·',
  8902: '*',
  8917: '#',
  8920: '<<<',
  8921: '>>>',
  8943: '...',
  9001: '<',
  9002: '>',
  9216: 'NUL',
  9217: 'SOH',
  9218: 'STX',
  9219: 'ETX',
  9220: 'EOT',
  9221: 'ENQ',
  9222: 'ACK',
  9223: 'BEL',
  9224: 'BS',
  9225: 'HT',
  9226: 'LF',
  9227: 'VT',
  9228: 'FF',
  9229: 'CR',
  9230: 'SO',
  9231: 'SI',
  9232: 'DLE',
  9233: 'DC1',
  9234: 'DC2',
  9235: 'DC3',
  9236: 'DC4',
  9237: 'NAK',
  9238: 'SYN',
  9239: 'ETB',
  9240: 'CAN',
  9241: 'EM',
  9242: 'SUB',
  9243: 'ESC',
  9244: 'FS',
  9245: 'GS',
  9246: 'RS',
  9247: 'US',
  9248: 'SP',
  9249: 'DEL',
  9251: '_',
  9252: 'NL',
  9253: '///',
  9254: '?',
  9312: '(1)',
  9313: '(2)',
  9314: '(3)',
  9315: '(4)',
  9316: '(5)',
  9317: '(6)',
  9318: '(7)',
  9319: '(8)',
  9320: '(9)',
  9321: '(10)',
  9322: '(11)',
  9323: '(12)',
  9324: '(13)',
  9325: '(14)',
  9326: '(15)',
  9327: '(16)',
  9328: '(17)',
  9329: '(18)',
  9330: '(19)',
  9331: '(20)',
  9332: '(1)',
  9333: '(2)',
  9334: '(3)',
  9335: '(4)',
  9336: '(5)',
  9337: '(6)',
  9338: '(7)',
  9339: '(8)',
  9340: '(9)',
  9341: '(10)',
  9342: '(11)',
  9343: '(12)',
  9344: '(13)',
  9345: '(14)',
  9346: '(15)',
  9347: '(16)',
  9348: '(17)',
  9349: '(18)',
  9350: '(19)',
  9351: '(20)',
  9352: '1.',
  9353: '2.',
  9354: '3.',
  9355: '4.',
  9356: '5.',
  9357: '6.',
  9358: '7.',
  9359: '8.',
  9360: '9.',
  9361: '10.',
  9362: '11.',
  9363: '12.',
  9364: '13.',
  9365: '14.',
  9366: '15.',
  9367: '16.',
  9368: '17.',
  9369: '18.',
  9370: '19.',
  9371: '20.',
  9372: '(a)',
  9373: '(b)',
  9374: '(c)',
  9375: '(d)',
  9376: '(e)',
  9377: '(f)',
  9378: '(g)',
  9379: '(h)',
  9380: '(i)',
  9381: '(j)',
  9382: '(k)',
  9383: '(l)',
  9384: '(m)',
  9385: '(n)',
  9386: '(o)',
  9387: '(p)',
  9388: '(q)',
  9389: '(r)',
  9390: '(s)',
  9391: '(t)',
  9392: '(u)',
  9393: '(v)',
  9394: '(w)',
  9395: '(x)',
  9396: '(y)',
  9397: '(z)',
  9398: '(A)',
  9399: '(B)',
  9400: '(C)',
  9401: '(D)',
  9402: '(E)',
  9403: '(F)',
  9404: '(G)',
  9405: '(H)',
  9406: '(I)',
  9407: '(J)',
  9408: '(K)',
  9409: '(L)',
  9410: '(M)',
  9411: '(N)',
  9412: '(O)',
  9413: '(P)',
  9414: '(Q)',
  9415: '(R)',
  9416: '(S)',
  9417: '(T)',
  9418: '(U)',
  9419: '(V)',
  9420: '(W)',
  9421: '(X)',
  9422: '(Y)',
  9423: '(Z)',
  9424: '(a)',
  9425: '(b)',
  9426: '(c)',
  9427: '(d)',
  9428: '(e)',
  9429: '(f)',
  9430: '(g)',
  9431: '(h)',
  9432: '(i)',
  9433: '(j)',
  9434: '(k)',
  9435: '(l)',
  9436: '(m)',
  9437: '(n)',
  9438: '(o)',
  9439: '(p)',
  9440: '(q)',
  9441: '(r)',
  9442: '(s)',
  9443: '(t)',
  9444: '(u)',
  9445: '(v)',
  9446: '(w)',
  9447: '(x)',
  9448: '(y)',
  9449: '(z)',
  9450: '(0)',
  9472: '-',
  9473: '=',
  9474: '|',
  9475: '|',
  9476: '-',
  9477: '=',
  9478: '|',
  9479: '|',
  9480: '-',
  9481: '=',
  9482: '|',
  9483: '|',
  9484: '+',
  9485: '+',
  9486: '+',
  9487: '+',
  9488: '+',
  9489: '+',
  9490: '+',
  9491: '+',
  9492: '+',
  9493: '+',
  9494: '+',
  9495: '+',
  9496: '+',
  9497: '+',
  9498: '+',
  9499: '+',
  9500: '+',
  9501: '+',
  9502: '+',
  9503: '+',
  9504: '+',
  9505: '+',
  9506: '+',
  9507: '+',
  9508: '+',
  9509: '+',
  9510: '+',
  9511: '+',
  9512: '+',
  9513: '+',
  9514: '+',
  9515: '+',
  9516: '+',
  9517: '+',
  9518: '+',
  9519: '+',
  9520: '+',
  9521: '+',
  9522: '+',
  9523: '+',
  9524: '+',
  9525: '+',
  9526: '+',
  9527: '+',
  9528: '+',
  9529: '+',
  9530: '+',
  9531: '+',
  9532: '+',
  9533: '+',
  9534: '+',
  9535: '+',
  9536: '+',
  9537: '+',
  9538: '+',
  9539: '+',
  9540: '+',
  9541: '+',
  9542: '+',
  9543: '+',
  9544: '+',
  9545: '+',
  9546: '+',
  9547: '+',
  9548: '-',
  9549: '=',
  9550: '|',
  9551: '|',
  9552: '=',
  9553: '|',
  9554: '+',
  9555: '+',
  9556: '+',
  9557: '+',
  9558: '+',
  9559: '+',
  9560: '+',
  9561: '+',
  9562: '+',
  9563: '+',
  9564: '+',
  9565: '+',
  9566: '+',
  9567: '+',
  9568: '+',
  9569: '+',
  9570: '+',
  9571: '+',
  9572: '+',
  9573: '+',
  9574: '+',
  9575: '+',
  9576: '+',
  9577: '+',
  9578: '+',
  9579: '+',
  9580: '+',
  9581: '+',
  9582: '+',
  9583: '+',
  9584: '+',
  9585: '/',
  9586: '\\',
  9587: 'X',
  9596: '-',
  9597: '|',
  9598: '-',
  9599: '|',
  9675: 'o',
  9702: 'o',
  9733: '*',
  9734: '*',
  9746: 'X',
  9747: 'X',
  9785: ':-(',
  9786: ':-)',
  9787: '(-:',
  9837: 'b',
  9839: '#',
  9985: '%<',
  9986: '%<',
  9987: '%<',
  9988: '%<',
  9996: 'V',
  10003: '√',
  10004: '√',
  10005: 'x',
  10006: 'x',
  10007: 'X',
  10008: 'X',
  10009: '+',
  10010: '+',
  10011: '+',
  10012: '+',
  10013: '+',
  10014: '+',
  10015: '+',
  10016: '+',
  10017: '*',
  10018: '+',
  10019: '+',
  10020: '+',
  10021: '+',
  10022: '+',
  10023: '+',
  10025: '*',
  10026: '*',
  10027: '*',
  10028: '*',
  10029: '*',
  10030: '*',
  10031: '*',
  10032: '*',
  10033: '*',
  10034: '*',
  10035: '*',
  10036: '*',
  10037: '*',
  10038: '*',
  10039: '*',
  10040: '*',
  10041: '*',
  10042: '*',
  10043: '*',
  10044: '*',
  10045: '*',
  10046: '*',
  10047: '*',
  10048: '*',
  10049: '*',
  10050: '*',
  10051: '*',
  10052: '*',
  10053: '*',
  10054: '*',
  10055: '*',
  10056: '*',
  10057: '*',
  10058: '*',
  10059: '*',
  64256: 'ff',
  64257: 'fi',
  64258: 'fl',
  64259: 'ffi',
  64260: 'ffl',
  64261: 'ſt',
  64262: 'st',
  65279: '',
  65533: '?',
}

short_table = {
  160: ' ',
  161: '!',
  162: 'c',
  163: 'GBP',
  165: 'Y',
  166: '|',
  167: 'S',
  168: '"',
  169: 'c',
  170: 'a',
  171: '<<',
  172: '-',
  173: '-',
  174: '(R)',
  175: '-',
  176: ' ',
  177: '+/-',
  178: '2',
  179: '3',
  180: "'",
  181: 'u',
  182: 'P',
  183: '.',
  184: ',',
  185: '1',
  186: 'o',
  187: '>>',
  188: ' 1/4',
  189: ' 1/2',
  190: ' 3/4',
  191: '?',
  192: 'A',
  193: 'A',
  194: 'A',
  195: 'A',
  196: 'A',
  197: 'A',
  198: 'A',
  199: 'C',
  200: 'E',
  201: 'E',
  202: 'E',
  203: 'E',
  204: 'I',
  205: 'I',
  206: 'I',
  207: 'I',
  208: 'D',
  209: 'N',
  210: 'O',
  211: 'O',
  212: 'O',
  213: 'O',
  214: 'O',
  215: 'x',
  216: 'O',
  217: 'U',
  218: 'U',
  219: 'U',
  220: 'U',
  221: 'Y',
  222: 'Th',
  223: 'β',
  224: 'a',
  225: 'a',
  226: 'a',
  227: 'a',
  228: 'a',
  229: 'a',
  230: 'a',
  231: 'c',
  232: 'e',
  233: 'e',
  234: 'e',
  235: 'e',
  236: 'i',
  237: 'i',
  238: 'i',
  239: 'i',
  240: 'd',
  241: 'n',
  242: 'o',
  243: 'o',
  244: 'o',
  245: 'o',
  246: 'o',
  247: ':',
  248: 'o',
  249: 'u',
  250: 'u',
  251: 'u',
  252: 'u',
  253: 'y',
  254: 'th',
  255: 'y',
  256: 'A',
  257: 'a',
  258: 'A',
  259: 'a',
  260: 'A',
  261: 'a',
  262: 'C',
  263: 'c',
  264: 'C',
  265: 'c',
  266: 'C',
  267: 'c',
  268: 'C',
  269: 'c',
  270: 'D',
  271: 'd',
  272: 'D',
  273: 'd',
  274: 'E',
  275: 'e',
  276: 'E',
  277: 'e',
  278: 'E',
  279: 'e',
  280: 'E',
  281: 'e',
  282: 'E',
  283: 'e',
  284: 'G',
  285: 'g',
  286: 'G',
  287: 'g',
  288: 'G',
  289: 'g',
  290: 'G',
  291: 'g',
  292: 'H',
  293: 'h',
  294: 'H',
  295: 'h',
  296: 'I',
  297: 'i',
  298: 'I',
  299: 'i',
  300: 'I',
  301: 'i',
  302: 'I',
  303: 'i',
  304: 'I',
  305: 'i',
  306: 'IJ',
  307: 'ij',
  308: 'J',
  309: 'j',
  310: 'K',
  311: 'k',
  312: 'k',
  313: 'L',
  314: 'l',
  315: 'L',
  316: 'l',
  317: 'L',
  318: 'l',
  319: 'L.',
  320: 'l.',
  321: 'L',
  322: 'l',
  323: 'N',
  324: 'n',
  325: 'N',
  326: 'n',
  327: 'N',
  328: 'n',
  329: "'n",
  330: 'N',
  331: 'n',
  332: 'O',
  333: 'o',
  334: 'O',
  335: 'o',
  336: 'O',
  337: 'o',
  338: 'OE',
  339: 'oe',
  340: 'R',
  341: 'r',
  342: 'R',
  343: 'r',
  344: 'R',
  345: 'r',
  346: 'S',
  347: 's',
  348: 'S',
  349: 's',
  350: 'S',
  351: 's',
  352: 'S',
  353: 's',
  354: 'T',
  355: 't',
  356: 'T',
  357: 't',
  358: 'T',
  359: 't',
  360: 'U',
  361: 'u',
  362: 'U',
  363: 'u',
  364: 'U',
  365: 'u',
  366: 'U',
  367: 'u',
  368: 'U',
  369: 'u',
  370: 'U',
  371: 'u',
  372: 'W',
  373: 'w',
  374: 'Y',
  375: 'y',
  376: 'Y',
  377: 'Z',
  378: 'z',
  379: 'Z',
  380: 'z',
  381: 'Z',
  382: 'z',
  383: 's',
  402: 'f',
  416: 'O',
  417: 'o',
  431: 'U',
  432: 'u',
  536: 'S',
  537: 's',
  538: 'T',
  539: 't',
  697: "'",
  699: '‘',
  700: "'",
  701: '‛',
  710: '^',
  712: "'",
  713: '¯',
  716: ',',
  720: ':',
  730: '°',
  732: '~',
  733: '"',
  884: "'",
  885: ',',
  894: ';',
  7682: 'B',
  7683: 'b',
  7690: 'D',
  7691: 'd',
  7710: 'F',
  7711: 'f',
  7744: 'M',
  7745: 'm',
  7766: 'P',
  7767: 'p',
  7776: 'S',
  7777: 's',
  7786: 'T',
  7787: 't',
  7808: 'W',
  7809: 'w',
  7810: 'W',
  7811: 'w',
  7812: 'W',
  7813: 'w',
  7918: 'U',
  7919: 'u',
  7922: 'Y',
  7923: 'y',
  8192: ' ',
  8193: '  ',
  8194: ' ',
  8195: '  ',
  8196: ' ',
  8197: ' ',
  8198: ' ',
  8199: ' ',
  8200: ' ',
  8201: ' ',
  8202: '',
  8203: '',
  8204: '',
  8205: '',
  8206: '',
  8207: '',
  8208: '-',
  8209: '-',
  8210: '-',
  8211: '-',
  8212: '--',
  8213: '--',
  8214: '||',
  8215: '_',
  8216: "'",
  8217: "'",
  8218: "'",
  8219: "'",
  8220: '"',
  8221: '"',
  8222: '"',
  8223: '"',
  8224: '+',
  8225: '++',
  8226: 'o',
  8227: '>',
  8228: '.',
  8229: '..',
  8230: '...',
  8231: '-',
  8234: '',
  8235: '',
  8236: '',
  8237: '',
  8238: '',
  8239: ' ',
  8240: ' 0/00',
  8242: "'",
  8243: '"',
  8244: "'''",
  8245: '`',
  8246: '``',
  8247: '```',
  8249: '<',
  8250: '>',
  8252: '!!',
  8254: '-',
  8259: '-',
  8260: '/',
  8264: '?!',
  8265: '!?',
  8266: '7',
  8304: '0',
  8308: '4',
  8309: '5',
  8310: '6',
  8311: '7',
  8312: '8',
  8313: '9',
  8314: '+',
  8315: '-',
  8316: '=',
  8317: '(',
  8318: ')',
  8319: 'n',
  8320: '0',
  8321: '1',
  8322: '2',
  8323: '3',
  8324: '4',
  8325: '5',
  8326: '6',
  8327: '7',
  8328: '8',
  8329: '9',
  8330: '+',
  8331: '-',
  8332: '=',
  8333: '(',
  8334: ')',
  8364: 'E',
  8448: 'a/c',
  8449: 'a/s',
  8451: 'C',
  8453: 'c/o',
  8454: 'c/u',
  8457: 'F',
  8467: 'l',
  8470: 'No',
  8471: '(P)',
  8480: '[SM]',
  8481: 'TEL',
  8482: '[TM]',
  8486: 'ohm',
  8490: 'K',
  8491: 'Å',
  8494: 'e',
  8531: ' 1/3',
  8532: ' 2/3',
  8533: ' 1/5',
  8534: ' 2/5',
  8535: ' 3/5',
  8536: ' 4/5',
  8537: ' 1/6',
  8538: ' 5/6',
  8539: ' 1/8',
  8540: ' 3/8',
  8541: ' 5/8',
  8542: ' 7/8',
  8543: ' 1/',
  8544: 'I',
  8545: 'II',
  8546: 'III',
  8547: 'IV',
  8548: 'V',
  8549: 'VI',
  8550: 'VII',
  8551: 'VIII',
  8552: 'IX',
  8553: 'X',
  8554: 'XI',
  8555: 'XII',
  8556: 'L',
  8557: 'C',
  8558: 'D',
  8559: 'M',
  8560: 'i',
  8561: 'ii',
  8562: 'iii',
  8563: 'iv',
  8564: 'v',
  8565: 'vi',
  8566: 'vii',
  8567: 'viii',
  8568: 'ix',
  8569: 'x',
  8570: 'xi',
  8571: 'xii',
  8572: 'l',
  8573: 'c',
  8574: 'd',
  8575: 'm',
  8592: '<-',
  8593: '^',
  8594: '->',
  8595: 'v',
  8596: '<->',
  8656: '<=',
  8658: '=>',
  8660: '<=>',
  8722: '-',
  8725: '/',
  8726: '\\',
  8727: '*',
  8728: 'o',
  8729: '·',
  8734: 'inf',
  8739: '|',
  8741: '||',
  8758: ':',
  8764: '~',
  8800: '/=',
  8801: '=',
  8804: '<=',
  8805: '>=',
  8810: '<<',
  8811: '>>',
  8853: '(+)',
  8854: '(-)',
  8855: '(x)',
  8856: '(/)',
  8866: '|-',
  8867: '-|',
  8870: '|-',
  8871: '|=',
  8872: '|=',
  8873: '||-',
  8901: '·',
  8902: '*',
  8917: '#',
  8920: '<<<',
  8921: '>>>',
  8943: '...',
  9001: '<',
  9002: '>',
  9216: 'NUL',
  9217: 'SOH',
  9218: 'STX',
  9219: 'ETX',
  9220: 'EOT',
  9221: 'ENQ',
  9222: 'ACK',
  9223: 'BEL',
  9224: 'BS',
  9225: 'HT',
  9226: 'LF',
  9227: 'VT',
  9228: 'FF',
  9229: 'CR',
  9230: 'SO',
  9231: 'SI',
  9232: 'DLE',
  9233: 'DC1',
  9234: 'DC2',
  9235: 'DC3',
  9236: 'DC4',
  9237: 'NAK',
  9238: 'SYN',
  9239: 'ETB',
  9240: 'CAN',
  9241: 'EM',
  9242: 'SUB',
  9243: 'ESC',
  9244: 'FS',
  9245: 'GS',
  9246: 'RS',
  9247: 'US',
  9248: 'SP',
  9249: 'DEL',
  9251: '_',
  9252: 'NL',
  9253: '///',
  9254: '?',
  9312: '1',
  9313: '2',
  9314: '3',
  9315: '4',
  9316: '5',
  9317: '6',
  9318: '7',
  9319: '8',
  9320: '9',
  9321: '(10)',
  9322: '(11)',
  9323: '(12)',
  9324: '(13)',
  9325: '(14)',
  9326: '(15)',
  9327: '(16)',
  9328: '(17)',
  9329: '(18)',
  9330: '(19)',
  9331: '(20)',
  9332: '1',
  9333: '2',
  9334: '3',
  9335: '4',
  9336: '5',
  9337: '6',
  9338: '7',
  9339: '8',
  9340: '9',
  9341: '(10)',
  9342: '(11)',
  9343: '(12)',
  9344: '(13)',
  9345: '(14)',
  9346: '(15)',
  9347: '(16)',
  9348: '(17)',
  9349: '(18)',
  9350: '(19)',
  9351: '(20)',
  9352: '1',
  9353: '2',
  9354: '3',
  9355: '4',
  9356: '5',
  9357: '6',
  9358: '7',
  9359: '8',
  9360: '9',
  9361: '10.',
  9362: '11.',
  9363: '12.',
  9364: '13.',
  9365: '14.',
  9366: '15.',
  9367: '16.',
  9368: '17.',
  9369: '18.',
  9370: '19.',
  9371: '20.',
  9372: 'a',
  9373: 'b',
  9374: 'c',
  9375: 'd',
  9376: 'e',
  9377: 'f',
  9378: 'g',
  9379: 'h',
  9380: 'i',
  9381: 'j',
  9382: 'k',
  9383: 'l',
  9384: 'm',
  9385: 'n',
  9386: 'o',
  9387: 'p',
  9388: 'q',
  9389: 'r',
  9390: 's',
  9391: 't',
  9392: 'u',
  9393: 'v',
  9394: 'w',
  9395: 'x',
  9396: 'y',
  9397: 'z',
  9398: 'A',
  9399: 'B',
  9400: 'C',
  9401: 'D',
  9402: 'E',
  9403: 'F',
  9404: 'G',
  9405: 'H',
  9406: 'I',
  9407: 'J',
  9408: 'K',
  9409: 'L',
  9410: 'M',
  9411: 'N',
  9412: 'O',
  9413: 'P',
  9414: 'Q',
  9415: 'R',
  9416: 'S',
  9417: 'T',
  9418: 'U',
  9419: 'V',
  9420: 'W',
  9421: 'X',
  9422: 'Y',
  9423: 'Z',
  9424: 'a',
  9425: 'b',
  9426: 'c',
  9427: 'd',
  9428: 'e',
  9429: 'f',
  9430: 'g',
  9431: 'h',
  9432: 'i',
  9433: 'j',
  9434: 'k',
  9435: 'l',
  9436: 'm',
  9437: 'n',
  9438: 'o',
  9439: 'p',
  9440: 'q',
  9441: 'r',
  9442: 's',
  9443: 't',
  9444: 'u',
  9445: 'v',
  9446: 'w',
  9447: 'x',
  9448: 'y',
  9449: 'z',
  9450: '0',
  9472: '-',
  9473: '=',
  9474: '|',
  9475: '|',
  9476: '-',
  9477: '=',
  9478: '|',
  9479: '|',
  9480: '-',
  9481: '=',
  9482: '|',
  9483: '|',
  9484: '+',
  9485: '+',
  9486: '+',
  9487: '+',
  9488: '+',
  9489: '+',
  9490: '+',
  9491: '+',
  9492: '+',
  9493: '+',
  9494: '+',
  9495: '+',
  9496: '+',
  9497: '+',
  9498: '+',
  9499: '+',
  9500: '+',
  9501: '+',
  9502: '+',
  9503: '+',
  9504: '+',
  9505: '+',
  9506: '+',
  9507: '+',
  9508: '+',
  9509: '+',
  9510: '+',
  9511: '+',
  9512: '+',
  9513: '+',
  9514: '+',
  9515: '+',
  9516: '+',
  9517: '+',
  9518: '+',
  9519: '+',
  9520: '+',
  9521: '+',
  9522: '+',
  9523: '+',
  9524: '+',
  9525: '+',
  9526: '+',
  9527: '+',
  9528: '+',
  9529: '+',
  9530: '+',
  9531: '+',
  9532: '+',
  9533: '+',
  9534: '+',
  9535: '+',
  9536: '+',
  9537: '+',
  9538: '+',
  9539: '+',
  9540: '+',
  9541: '+',
  9542: '+',
  9543: '+',
  9544: '+',
  9545: '+',
  9546: '+',
  9547: '+',
  9548: '-',
  9549: '=',
  9550: '|',
  9551: '|',
  9552: '=',
  9553: '|',
  9554: '+',
  9555: '+',
  9556: '+',
  9557: '+',
  9558: '+',
  9559: '+',
  9560: '+',
  9561: '+',
  9562: '+',
  9563: '+',
  9564: '+',
  9565: '+',
  9566: '+',
  9567: '+',
  9568: '+',
  9569: '+',
  9570: '+',
  9571: '+',
  9572: '+',
  9573: '+',
  9574: '+',
  9575: '+',
  9576: '+',
  9577: '+',
  9578: '+',
  9579: '+',
  9580: '+',
  9581: '+',
  9582: '+',
  9583: '+',
  9584: '+',
  9585: '/',
  9586: '\\',
  9587: 'X',
  9596: '-',
  9597: '|',
  9598: '-',
  9599: '|',
  9675: 'o',
  9702: 'o',
  9733: '*',
  9734: '*',
  9746: 'X',
  9747: 'X',
  9785: ':-(',
  9786: ':-)',
  9787: '(-:',
  9837: 'b',
  9839: '#',
  9985: '%<',
  9986: '%<',
  9987: '%<',
  9988: '%<',
  9996: 'V',
  10003: '√',
  10004: '√',
  10005: 'x',
  10006: 'x',
  10007: 'X',
  10008: 'X',
  10009: '+',
  10010: '+',
  10011: '+',
  10012: '+',
  10013: '+',
  10014: '+',
  10015: '+',
  10016: '+',
  10017: '*',
  10018: '+',
  10019: '+',
  10020: '+',
  10021: '+',
  10022: '+',
  10023: '+',
  10025: '*',
  10026: '*',
  10027: '*',
  10028: '*',
  10029: '*',
  10030: '*',
  10031: '*',
  10032: '*',
  10033: '*',
  10034: '*',
  10035: '*',
  10036: '*',
  10037: '*',
  10038: '*',
  10039: '*',
  10040: '*',
  10041: '*',
  10042: '*',
  10043: '*',
  10044: '*',
  10045: '*',
  10046: '*',
  10047: '*',
  10048: '*',
  10049: '*',
  10050: '*',
  10051: '*',
  10052: '*',
  10053: '*',
  10054: '*',
  10055: '*',
  10056: '*',
  10057: '*',
  10058: '*',
  10059: '*',
  64256: 'ff',
  64257: 'fi',
  64258: 'fl',
  64259: 'ffi',
  64260: 'ffl',
  64261: 'st',
  64262: 'st',
  65279: '',
  65533: '?',
}

single_table = {
  160: ' ',
  161: '!',
  162: 'c',
  165: 'Y',
  166: '|',
  167: 'S',
  168: '"',
  169: 'c',
  170: 'a',
  172: '-',
  173: '-',
  175: '-',
  176: ' ',
  178: '2',
  179: '3',
  180: "'",
  181: 'u',
  182: 'P',
  183: '.',
  184: ',',
  185: '1',
  186: 'o',
  191: '?',
  192: 'A',
  193: 'A',
  194: 'A',
  195: 'A',
  196: 'A',
  197: 'A',
  198: 'A',
  199: 'C',
  200: 'E',
  201: 'E',
  202: 'E',
  203: 'E',
  204: 'I',
  205: 'I',
  206: 'I',
  207: 'I',
  208: 'D',
  209: 'N',
  210: 'O',
  211: 'O',
  212: 'O',
  213: 'O',
  214: 'O',
  215: 'x',
  216: 'O',
  217: 'U',
  218: 'U',
  219: 'U',
  220: 'U',
  221: 'Y',
  223: 'β',
  224: 'a',
  225: 'a',
  226: 'a',
  227: 'a',
  228: 'a',
  229: 'a',
  230: 'a',
  231: 'c',
  232: 'e',
  233: 'e',
  234: 'e',
  235: 'e',
  236: 'i',
  237: 'i',
  238: 'i',
  239: 'i',
  240: 'd',
  241: 'n',
  242: 'o',
  243: 'o',
  244: 'o',
  245: 'o',
  246: 'o',
  247: ':',
  248: 'o',
  249: 'u',
  250: 'u',
  251: 'u',
  252: 'u',
  253: 'y',
  255: 'y',
  256: 'A',
  257: 'a',
  258: 'A',
  259: 'a',
  260: 'A',
  261: 'a',
  262: 'C',
  263: 'c',
  264: 'C',
  265: 'c',
  266: 'C',
  267: 'c',
  268: 'C',
  269: 'c',
  270: 'D',
  271: 'd',
  272: 'D',
  273: 'd',
  274: 'E',
  275: 'e',
  276: 'E',
  277: 'e',
  278: 'E',
  279: 'e',
  280: 'E',
  281: 'e',
  282: 'E',
  283: 'e',
  284: 'G',
  285: 'g',
  286: 'G',
  287: 'g',
  288: 'G',
  289: 'g',
  290: 'G',
  291: 'g',
  292: 'H',
  293: 'h',
  294: 'H',
  295: 'h',
  296: 'I',
  297: 'i',
  298: 'I',
  299: 'i',
  300: 'I',
  301: 'i',
  302: 'I',
  303: 'i',
  304: 'I',
  305: 'i',
  308: 'J',
  309: 'j',
  310: 'K',
  311: 'k',
  312: 'k',
  313: 'L',
  314: 'l',
  315: 'L',
  316: 'l',
  317: 'L',
  318: 'l',
  321: 'L',
  322: 'l',
  323: 'N',
  324: 'n',
  325: 'N',
  326: 'n',
  327: 'N',
  328: 'n',
  330: 'N',
  331: 'n',
  332: 'O',
  333: 'o',
  334: 'O',
  335: 'o',
  336: 'O',
  337: 'o',
  340: 'R',
  341: 'r',
  342: 'R',
  343: 'r',
  344: 'R',
  345: 'r',
  346: 'S',
  347: 's',
  348: 'S',
  349: 's',
  350: 'S',
  351: 's',
  352: 'S',
  353: 's',
  354: 'T',
  355: 't',
  356: 'T',
  357: 't',
  358: 'T',
  359: 't',
  360: 'U',
  361: 'u',
  362: 'U',
  363: 'u',
  364: 'U',
  365: 'u',
  366: 'U',
  367: 'u',
  368: 'U',
  369: 'u',
  370: 'U',
  371: 'u',
  372: 'W',
  373: 'w',
  374: 'Y',
  375: 'y',
  376: 'Y',
  377: 'Z',
  378: 'z',
  379: 'Z',
  380: 'z',
  381: 'Z',
  382: 'z',
  383: 's',
  402: 'f',
  416: 'O',
  417: 'o',
  431: 'U',
  432: 'u',
  536: 'S',
  537: 's',
  538: 'T',
  539: 't',
  697: "'",
  699: '‘',
  700: "'",
  701: '‛',
  710: '^',
  712: "'",
  713: '¯',
  716: ',',
  720: ':',
  730: '°',
  732: '~',
  733: '"',
  884: "'",
  885: ',',
  894: ';',
  7682: 'B',
  7683: 'b',
  7690: 'D',
  7691: 'd',
  7710: 'F',
  7711: 'f',
  7744: 'M',
  7745: 'm',
  7766: 'P',
  7767: 'p',
  7776: 'S',
  7777: 's',
  7786: 'T',
  7787: 't',
  7808: 'W',
  7809: 'w',
  7810: 'W',
  7811: 'w',
  7812: 'W',
  7813: 'w',
  7918: 'U',
  7919: 'u',
  7922: 'Y',
  7923: 'y',
  8192: ' ',
  8194: ' ',
  8196: ' ',
  8197: ' ',
  8198: ' ',
  8199: ' ',
  8200: ' ',
  8201: ' ',
  8208: '-',
  8209: '-',
  8210: '-',
  8211: '-',
  8215: '_',
  8216: "'",
  8217: "'",
  8218: "'",
  8219: "'",
  8220: '"',
  8221: '"',
  8222: '"',
  8223: '"',
  8224: '+',
  8226: 'o',
  8227: '>',
  8228: '.',
  8231: '-',
  8239: ' ',
  8242: "'",
  8243: '"',
  8245: '`',
  8249: '<',
  8250: '>',
  8254: '-',
  8259: '-',
  8260: '/',
  8266: '7',
  8304: '0',
  8308: '4',
  8309: '5',
  8310: '6',
  8311: '7',
  8312: '8',
  8313: '9',
  8314: '+',
  8315: '-',
  8316: '=',
  8317: '(',
  8318: ')',
  8319: 'n',
  8320: '0',
  8321: '1',
  8322: '2',
  8323: '3',
  8324: '4',
  8325: '5',
  8326: '6',
  8327: '7',
  8328: '8',
  8329: '9',
  8330: '+',
  8331: '-',
  8332: '=',
  8333: '(',
  8334: ')',
  8364: 'E',
  8451: 'C',
  8457: 'F',
  8467: 'l',
  8490: 'K',
  8491: 'Å',
  8494: 'e',
  8544: 'I',
  8548: 'V',
  8553: 'X',
  8556: 'L',
  8557: 'C',
  8558: 'D',
  8559: 'M',
  8560: 'i',
  8564: 'v',
  8569: 'x',
  8572: 'l',
  8573: 'c',
  8574: 'd',
  8575: 'm',
  8593: '^',
  8595: 'v',
  8722: '-',
  8725: '/',
  8726: '\\',
  8727: '*',
  8728: 'o',
  8729: '·',
  8739: '|',
  8758: ':',
  8764: '~',
  8801: '=',
  8901: '·',
  8902: '*',
  8917: '#',
  9001: '<',
  9002: '>',
  9251: '_',
  9254: '?',
  9312: '1',
  9313: '2',
  9314: '3',
  9315: '4',
  9316: '5',
  9317: '6',
  9318: '7',
  9319: '8',
  9320: '9',
  9332: '1',
  9333: '2',
  9334: '3',
  9335: '4',
  9336: '5',
  9337: '6',
  9338: '7',
  9339: '8',
  9340: '9',
  9352: '1',
  9353: '2',
  9354: '3',
  9355: '4',
  9356: '5',
  9357: '6',
  9358: '7',
  9359: '8',
  9360: '9',
  9372: 'a',
  9373: 'b',
  9374: 'c',
  9375: 'd',
  9376: 'e',
  9377: 'f',
  9378: 'g',
  9379: 'h',
  9380: 'i',
  9381: 'j',
  9382: 'k',
  9383: 'l',
  9384: 'm',
  9385: 'n',
  9386: 'o',
  9387: 'p',
  9388: 'q',
  9389: 'r',
  9390: 's',
  9391: 't',
  9392: 'u',
  9393: 'v',
  9394: 'w',
  9395: 'x',
  9396: 'y',
  9397: 'z',
  9398: 'A',
  9399: 'B',
  9400: 'C',
  9401: 'D',
  9402: 'E',
  9403: 'F',
  9404: 'G',
  9405: 'H',
  9406: 'I',
  9407: 'J',
  9408: 'K',
  9409: 'L',
  9410: 'M',
  9411: 'N',
  9412: 'O',
  9413: 'P',
  9414: 'Q',
  9415: 'R',
  9416: 'S',
  9417: 'T',
  9418: 'U',
  9419: 'V',
  9420: 'W',
  9421: 'X',
  9422: 'Y',
  9423: 'Z',
  9424: 'a',
  9425: 'b',
  9426: 'c',
  9427: 'd',
  9428: 'e',
  9429: 'f',
  9430: 'g',
  9431: 'h',
  9432: 'i',
  9433: 'j',
  9434: 'k',
  9435: 'l',
  9436: 'm',
  9437: 'n',
  9438: 'o',
  9439: 'p',
  9440: 'q',
  9441: 'r',
  9442: 's',
  9443: 't',
  9444: 'u',
  9445: 'v',
  9446: 'w',
  9447: 'x',
  9448: 'y',
  9449: 'z',
  9450: '0',
  9472: '-',
  9473: '=',
  9474: '|',
  9475: '|',
  9476: '-',
  9477: '=',
  9478: '|',
  9479: '|',
  9480: '-',
  9481: '=',
  9482: '|',
  9483: '|',
  9484: '+',
  9485: '+',
  9486: '+',
  9487: '+',
  9488: '+',
  9489: '+',
  9490: '+',
  9491: '+',
  9492: '+',
  9493: '+',
  9494: '+',
  9495: '+',
  9496: '+',
  9497: '+',
  9498: '+',
  9499: '+',
  9500: '+',
  9501: '+',
  9502: '+',
  9503: '+',
  9504: '+',
  9505: '+',
  9506: '+',
  9507: '+',
  9508: '+',
  9509: '+',
  9510: '+',
  9511: '+',
  9512: '+',
  9513: '+',
  9514: '+',
  9515: '+',
  9516: '+',
  9517: '+',
  9518: '+',
  9519: '+',
  9520: '+',
  9521: '+',
  9522: '+',
  9523: '+',
  9524: '+',
  9525: '+',
  9526: '+',
  9527: '+',
  9528: '+',
  9529: '+',
  9530: '+',
  9531: '+',
  9532: '+',
  9533: '+',
  9534: '+',
  9535: '+',
  9536: '+',
  9537: '+',
  9538: '+',
  9539: '+',
  9540: '+',
  9541: '+',
  9542: '+',
  9543: '+',
  9544: '+',
  9545: '+',
  9546: '+',
  9547: '+',
  9548: '-',
  9549: '=',
  9550: '|',
  9551: '|',
  9552: '=',
  9553: '|',
  9554: '+',
  9555: '+',
  9556: '+',
  9557: '+',
  9558: '+',
  9559: '+',
  9560: '+',
  9561: '+',
  9562: '+',
  9563: '+',
  9564: '+',
  9565: '+',
  9566: '+',
  9567: '+',
  9568: '+',
  9569: '+',
  9570: '+',
  9571: '+',
  9572: '+',
  9573: '+',
  9574: '+',
  9575: '+',
  9576: '+',
  9577: '+',
  9578: '+',
  9579: '+',
  9580: '+',
  9581: '+',
  9582: '+',
  9583: '+',
  9584: '+',
  9585: '/',
  9586: '\\',
  9587: 'X',
  9596: '-',
  9597: '|',
  9598: '-',
  9599: '|',
  9675: 'o',
  9702: 'o',
  9733: '*',
  9734: '*',
  9746: 'X',
  9747: 'X',
  9837: 'b',
  9839: '#',
  9996: 'V',
  10003: '√',
  10004: '√',
  10005: 'x',
  10006: 'x',
  10007: 'X',
  10008: 'X',
  10009: '+',
  10010: '+',
  10011: '+',
  10012: '+',
  10013: '+',
  10014: '+',
  10015: '+',
  10016: '+',
  10017: '*',
  10018: '+',
  10019: '+',
  10020: '+',
  10021: '+',
  10022: '+',
  10023: '+',
  10025: '*',
  10026: '*',
  10027: '*',
  10028: '*',
  10029: '*',
  10030: '*',
  10031: '*',
  10032: '*',
  10033: '*',
  10034: '*',
  10035: '*',
  10036: '*',
  10037: '*',
  10038: '*',
  10039: '*',
  10040: '*',
  10041: '*',
  10042: '*',
  10043: '*',
  10044: '*',
  10045: '*',
  10046: '*',
  10047: '*',
  10048: '*',
  10049: '*',
  10050: '*',
  10051: '*',
  10052: '*',
  10053: '*',
  10054: '*',
  10055: '*',
  10056: '*',
  10057: '*',
  10058: '*',
  10059: '*',
  65533: '?',
}


### <
