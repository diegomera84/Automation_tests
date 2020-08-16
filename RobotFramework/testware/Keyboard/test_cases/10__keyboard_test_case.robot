*** Settings ***
Documentation    Review of the different modules of the Keyboard of UE2020

Library       ../libraries/Keyboard_wrapper.py
Library       ../../commons/robot_framework_utilities.py
Force Tags    keyboard-tests

*** Test Cases ***
Validate Keyboard connection
    [Documentation]    Connect with the Keyboard 
    [Tags]    Keyboard-connection  command
    ${Keyboard_conection}=  keyboard initialize
    Should Be True  ${Keyboard_conection} 

Validate keyboard version
    [Documentation]    Compare the model and version 
    ...                of the current keyboard
    [Tags]    keyboard-version  command
    ${keyboard_version}=  get keyboard version
    Should Be Equal As Strings  ${keyboard_version}  1.2.0.0

Validate keyboard Random Number
    [Documentation]    Verify that the keyboard get a random number 
    [Tags]    keyboard-random  command
    ${keyboard_random}=  get keyboard randomnumber  ${3}
    Should Be True  ${keyboard_random}

Validate keyboard checkevent
    [Documentation]    Validate keyboard check event
    [Tags]    keyboard-checkevent  command
    ${keyboard_checkevent}=  check event
    should be True  ${keyboard_checkevent} 


