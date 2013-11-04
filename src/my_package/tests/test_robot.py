import unittest

import os
import robotsuite
from plone.app.testing import PLONE_ZSERVER
from plone.testing import layered

from plone.testing import Layer
from plone.app.testing import PLONE_FIXTURE

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from plone.testing import z2
from plone.app.testing import FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

dirname = os.path.dirname(__file__)
files = os.listdir(dirname)
tests = [f for f in files if f.startswith('test_') and f.endswith('.robot')]

class MyPackageFixture(Layer):
    defaultBases= (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(MyPackageFixture, self).setUpZope(app, configurationContext)
        import plone.app.linkintegrity
        self.loadZCML(package=plone.app.linkintegrity)
        z2.installProduct(app, 'plone.app.linkintegrity')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plone.app.linkintegrity')
    
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'plone.app.linkintegrity')

MY_PACKAGE_FIXTURE = MyPackageFixture()

MY_PACKAGE_ROBOT_TESTING = FunctionalTesting(bases=(MY_PACKAGE_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, PLONE_ZSERVER), name="my_pacackage:Robot",)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite(t),
                layer=MY_PACKAGE_ROBOT_TESTING)
        for t in tests
    ])
    return suite