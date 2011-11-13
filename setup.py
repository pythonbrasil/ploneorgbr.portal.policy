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
          'collective.contentrules.mailtogroup==1.2',
          'collective.contentrules.mailtolocalrole==1.1',
          'collective.recaptcha==1.1.3',
          'collective.simplesocial==1.6',
          'collective.twitter.accounts==1.0.1',
          'collective.twitter.action==1.0.1',
          'collective.watcherlist==0.3',
          #'jarn.xmpp.collaboration',
          'sc.social.like==0.9',
          'ploneorgbr.portal.theme==0.5',
          'ploneorg.kudobounty==0.1',
          'Products.Carousel==2.1',
          'Products.Doormat==0.7',
          'Products.PloneFormGen==1.7rc1',
          'Products.PloneHelpCenter==4.0b3',
          #'Products.PloneSoftwareCenter==1.6.2',
          'Products.Poi==2.0.2',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
