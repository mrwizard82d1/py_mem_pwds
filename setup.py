#! env python

from distutils.core import setup

import os

setup(name='MemorablePwds',
      version='1.0',
      description='Utilities to generate strong but easily memorized passwords.',
      author='Larry Jones',
      author_email='ljones5@slb.com',
      packages=['', 'tkui', 'pp2e_laj.gui.tools'],
      data_files=[('MemorablePwds', ['dict.txt']),])
 
