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
      keywords='plone policy',
      author='Comunidade Plone.org.br',
      author_email='contato@plone.org.br',
      url='http://www.plone.org.br/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneorgbr', 'ploneorgbr.portal'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          #'collective.cover',  # TODO: remove?
          'collective.contentrules.mailtogroup==1.2',  # TODO: remove?
          'collective.contentrules.mailtolocalrole==1.1',  # TODO: remove?
          'collective.geo.usersmap',
          'collective.loremipsum==0.5',
          'collective.ploneslimbar',
          'collective.recaptcha==1.1.3',
          'collective.simplesocial==1.6',
          'collective.twitter.accounts==1.0.1',
          'collective.twitter.action==1.0.1',
          'collective.watcherlist==0.3',  # TODO: remove?
          'sc.social.like==0.9.1',
          'psycopg2',
          'pas.plugins.sqlalchemy==0.3.1-dev',
          'plone.app.changeownership',
          'plone.namedfile',
          'ploneorgbr.portal.theme==0.5',
          'Products.Carousel==2.1',
          'Products.Doormat==0.7',  # TODO: remove?
          'Products.PloneFormGen==1.7.2',
          'Products.PloneHelpCenter==4.0b3',
          #'Products.PloneSoftwareCenter==1.6.2',
          'Products.Poi==2.0.2',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
