# -*- coding: utf-8 -*-
# File: config.py


__author__ = """Comunidade PloneOrgBr <contato@plone.org.br>"""
__docformat__ = 'plaintext'

# PRODUCTS format
# (name,locked,hidden,install,profile,runProfile)

PRODUCTS=[
         ('ploneorgbr.portal.policy',0,1,0,'ploneorgbr.portal.policy:uninstall',0),
         ('ploneorgbr.portal.theme',0,1,1,'ploneorgbr.portal.theme:default',1),
         ('ploneorgbr.portal.theme',0,1,0,'ploneorgbr.portal.theme:uninstall',0),
         ]
