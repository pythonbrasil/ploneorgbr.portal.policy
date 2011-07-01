# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("ploneorgbr", "portal", "policy", "version.txt")).read().strip()

setup(name='ploneorgbr.portal.policy',
      version=version,
      description="",
      long_description=open(os.path.join("ploneorgbr", "portal", "policy", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneorgbr', 'ploneorgbr.portal'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'ploneorgbr.portal.theme',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
