"""
Updates translitcodec/__init__.py with translation table information
built from the 'transtab' database.

:copyright: the translitcodec authors and developers, see AUTHORS.
:license: MIT, see LICENSE for more details.
"""
import csv
import os
import sys


csv.register_dialect('transtab', delimiter=';')


def read_table(path='transtab/transtab'):
    long, short, single = {}, {}, {}

    t = open(path)
    for line in t.readlines():
        if not line.startswith('<'):
            continue
        from_spec, raw_to = line.strip().split(' ', 1)
        from_ord = int(from_spec[2:-1], 16)
        if from_ord <= 128:
            continue

        raw = next(csv.reader([raw_to], 'transtab'))
        long_char = _unpack_uchrs(raw[0])
        if len(raw) < 2:
            short_char = long_char
        else:
            short_char = _unpack_uchrs(raw[1])

        long[from_ord] = long_char
        short[from_ord] = short_char
        if len(short_char) == 1:
            single[from_ord] = short_char
    return long, short, single


def _unpack_uchrs(packed):
    chunks = packed.replace('<U', ' ').strip().split()
    return u''.join(chr(int(spec[:-1], 16)) for spec in chunks)


def update_inclusion(long, short, single, path="translitcodec/__init__.py"):
    src = open(path)

    preamble, old, postamble = [], [], []
    bucket = preamble
    for line in src.readlines():
        if line.startswith('### <'):
            bucket = postamble
        bucket.append(line)
        if line.startswith('### >'):
            bucket = old
    src.close()

    rewrite = open(path, 'w')
    rewrite.writelines(preamble)
    rewrite.write("\n")
    _dump_dict(rewrite, 'long_table', long)
    _dump_dict(rewrite, 'short_table', short)
    _dump_dict(rewrite, 'single_table', single)
    rewrite.write("\n")
    rewrite.writelines(postamble)
    rewrite.close()


def _dump_dict(fh, name, data):
    fh.write("%s = {\n" % name)
    for pair in sorted(data.items()):
        fh.write("  %r: u%r,\n" % pair)
    fh.write("}\n\n")

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print("This script requires to be run under Python 3")
        sys.exit(-1)

    if not (os.path.exists('translitcodec') and os.path.exists('transtab')):
        print("Can not find translitcodec/ and transtab/ directories.")
        sys.exit(-1)
    tables = read_table()
    update_inclusion(*tables)
    print("Updated.")
