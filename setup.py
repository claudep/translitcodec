import codecs
from distutils.core import setup


readme = codecs.open('README', 'r', 'utf-8').read().encode('utf-8')

setup(name='translitcodec',
      version='0.2',
      description='Unicode to 8-bit charset transliteration codec',
      long_description=readme,
      author='Jason Kirtland',
      author_email='jek@discorporate.us',
      url='http://pypi.python.org/pypi/translitcodec/',
      packages=['translitcodec'],
      license='MIT License',
      )
