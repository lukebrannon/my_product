*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Test Cases ***

Plone Accessibility
    Goto homepage
    Click link  Accessibility
    Page should contain  Accessibility Statement

*** Keywords ***

Start browser
    Open browser  http://localhost:55001/plone/

Goto homepage
    Go to  http://localhost:55001/plone/
    Page should contain  Plone site