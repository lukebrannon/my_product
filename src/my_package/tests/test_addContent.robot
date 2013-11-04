*** Settings ***
Library  Selenium2Library  timeout=10  implicit_wait=0.5

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot
Variables  plone/app/testing/interfaces.py
Suite Setup  Open Test Browser
Suite Teardown  Close All Browsers


*** Variables ***

${title_selector} =  input#form-widgets-IBasic-title
${description_selector} =  textarea#form-widgets-IBasic-description
${title} =  Test Page
${description} =  'This is a test page.''

*** Test Cases ***

Site Admin Can Login
    Log in  ${SITE_OWNER_NAME}  ${SITE_OWNER_PASSWORD}
    Page should contain  Plone site
    Goto homepage
    Create Page
    Page Should Contain  ${title}

*** Keywords ***    
Goto homepage
    Go to  http://localhost:55001/plone/
    Page should contain  Plone site

Create Page
    Click Link  css=dl#plone-contentmenu-factories a
    Page Should Contain  Page
    Click Link  css=a#document
    Input Text  css=input#title  Test Page
    Click Button  Save
    Page Should Contain  Test Page