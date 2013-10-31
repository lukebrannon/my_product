import unittest

import robotsuite
from plone.app.testing import PLONE_ZSERVER
from plone.testing import layered


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("test_accessibility.robot"),
                layer=PLONE_ZSERVER),
    ])
    return suite