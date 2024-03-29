#! env python

from distutils.core import setup

import os

setup(
    name='MemorablePwds',
    version='1.1',
    author='Larry Jones',
    author_email='mrwizard82d2@earthlink.net',
    packages=['mem_pwds', 'mem_pwds.cmd',
              'mem_pwds.tkui', 'mem_pwds.wx', ],
    package_data={
        'mem_pwds': ['etc/*.TXT', 'etc/DICTION.ZIP'],
        },
    scripts = [
        'bin/cmd_memorable_pwds.py',
        'bin/tk_memorable_pwds.py',
        'bin/wx_memorable_pwds.py',
        ],
    url='http://www.earthlink.com/mrwizard82d1',
    description='Generate strong but easily memorized passwords.',
    long_description=open('README.txt').read()
    )
