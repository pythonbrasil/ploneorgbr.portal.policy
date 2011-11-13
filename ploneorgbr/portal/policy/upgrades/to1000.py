# -*- coding: utf-8 -*-
from zope import component
import logging
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import interfaces as gsinterfaces
from Products.GenericSetup.upgrade import listUpgradeSteps

from Products.ZCatalog.ProgressHandler import ZLogHandler

from ploneorgbr.portal.policy.config import PRODUCTS

def upgrade0to1000(context):
    """ Upgrade from version 0 to version 1000
    """
    setup = getToolByName(context, 'portal_setup')
    migration = getToolByName(context,'portal_migration')
    catalog = getToolByName(context,'portal_catalog')
    portal_properties = getToolByName(context,'portal_properties')
    qi = getToolByName(context,'portal_quickinstaller')

    # Install dependencies for this upgrade
    # List package names
    packages = [
        'Products.Carousel',
        'Products.Doormat',
        'Products.PloneHelpCenter',
        'ploneorg.kudobounty',
        'Products.PloneFormGen',
        #'Products.PloneSoftwareCenter',
        #'Products.Poi',
        'collective.contentrules.mailtogroup',
        'collective.contentrules.mailtolocalrole',
        'collective.recaptcha',
        'collective.simplesocial',
        'collective.twitter.action',
        'collective.watcherlist',
        'ploneorgbr.portal.theme',
        'sc.social.like',
    ]

    # (name,locked,hidden,install,profile,runProfile)
    dependencies = [(name,locked,hidden,profile) for name,locked,hidden,install,profile,runProfile in PRODUCTS if ((name in packages) and install)]

    for name,locked,hidden,profile in dependencies:
        qi.installProduct(name, locked=locked, hidden=hidden, profile=profile)

    # If we have blob and imaging installed
    # uncomment lines bellow
    # profiles = ['profile-plone.app.blob:file-replacement',
    #            'profile-plone.app.blob:image-replacement',
    #            ]
    # for profile in profiles:
    #     setup.runAllImportStepsFromProfile(profile)
