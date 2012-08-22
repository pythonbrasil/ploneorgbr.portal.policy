# -*- coding: utf-8 -*-
# File: config.py


__author__ = """Comunidade Plone.org.br <contato@plone.org.br>"""
__docformat__ = 'plaintext'

# PRODUCTS format
# (name, locked, hidden, install, profile, runProfile)

PRODUCTS = [
    ('collective.contentrules.mailtogroup', 0, 0, 1, 'collective.contentrules.mailtogroup:default', 1),
    ('collective.contentrules.mailtolocalrole', 0, 0, 1, 'collective.contentrules.mailtolocalrole:default', 1),
    #('collective.cover', 0, 0, 0, 'collective.cover:default', 0),
    ('collective.geo.usersmap', 0, 0, 1, 'collective.geo.usersmap:default', 1),
    ('collective.js.jqueryui', 0, 0, 0, 'collective.js.jqueryui:default', 0),
    ('collective.ploneslimbar', 0, 0, 1, 'collective.ploneslimbar:default', 1),
    ('collective.recaptcha', 0, 0, 1, 'collective.recaptcha:default', 1),
    ('collective.simplesocial',  0,  1,  1,  'collective.simplesocial:fbconnect',  1),
    ('collective.simplesocial',  0,  1,  0,  'collective.simplesocial:fbconnect_10_14',  0),
    ('collective.simplesocial',  0,  1,  0,  'collective.simplesocial:fbconnect_14_15b1',  0),
    ('collective.twitter.action', 0, 0, 1, 'collective.twitter.action:default', 1),
    ('collective.watcherlist', 0, 0, 1, 'collective.watcherlist:default', 1),
    ('ploneorgbr.portal.policy', 0, 1, 0, 'ploneorgbr.portal.policy:uninstall', 0),
    ('ploneorgbr.portal.theme', 0, 0, 1, 'ploneorgbr.portal.theme:default', 1),
    ('ploneorgbr.portal.theme', 0, 0, 0, 'ploneorgbr.portal.theme:uninstall', 0),
    ('sc.social.like', 0, 0, 1, 'sc.social.like:default', 1),
    ('sc.social.like', 0, 0, 0, 'sc.social.like:uninstall', 0),
    ('Products.Doormat', 0, 0, 1, 'Products.Doormat:default', 1),
    ('Products.Doormat', 0, 0, 0, 'Products.Doormat:uninstall', 0),
    ('Products.Carousel', 0, 0, 1, 'Products.Carousel:default', 1),
    ('Products.PloneFormGen', 0, 0, 1, 'Products.PloneFormGen:default', 1),
    ('Products.PloneHelpCenter', 0, 0, 1, 'Products.PloneHelpCenter:default', 1),
    #('Products.PloneSoftwareCenter', 0, 0, 1, 'Products.PloneSoftwareCenter:default', 1),
    ('Products.Poi', 0, 0, 0, 'Products.Poi:default', 1),
]
