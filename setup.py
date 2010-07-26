#! env python

from distutils.core import setup

import os

setup(
    name='MemorablePwds',
    version='1.0',
    author='Larry Jones',
    author_email='mrwizard82d2@earthlink.net',
    packages=['MemorablePwds', 'MemorablePwds.tkui'],
    data_files=[
        ('', ['share/MemorablePwds/DICT.TXT']),
        ('', ['share/MemorablePwds/DICTION.ZIP']),
        ('', ['share/MemorablePwds/TESTDICT.TXT']),
        ],
    url='http://www.earthlink.com/mrwizard82d1',
    description='Generate strong but easily memorized passwords.',
    long_description=open('README.txt').read()
    )
