import codecs
from distutils.core import setup
import sys


lines = codecs.open('README', 'r', 'utf-8').readlines()[3:]
lines.extend(codecs.open('CHANGES', 'r', 'utf-8').readlines()[1:])
desc = u''.join(lines).lstrip()
if sys.version_info < (3, 0):
    desc = desc.encode('utf-8')

import translitcodec
version = translitcodec.__version__

setup(name='translitcodec',
      version=version,
      description='Unicode to 8-bit charset transliteration codec',
      long_description=desc,
      author='Jason Kirtland',
      author_email='jek@discorporate.us',
      url='https://github.com/claudep/translitcodec',
      packages=['translitcodec'],
      license='MIT License',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          ],
      )
