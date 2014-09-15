#!/usr/bin/env python3

import inspect
import os
import setuptools

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))

def get_install_requirements(path):
    content = open(os.path.join(__location__, path)).read()
    return [req for req in content.split('\\n') if req != '']

def read(fname):
    return open(os.path.join(__location__, fname)).read()

def setup_package():
    install_reqs = get_install_requirements('requirements.txt')
    setuptools.setup(
        name='nsenter',
        version='0.1',
        url='https://github.com/zalando/python-nsenter',
        description='',
        author='Henning Jacobs',
        author_email='henning.jacobs@zalando.de',
        long_description=read('README.rst'),
        classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python'],
        test_suite='tests',
        packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
        install_requires=install_reqs,
        entry_points={'console_scripts': ['nsenter = nsenter:main']}
    )

if __name__ == '__main__':
    setup_package()