*** Settings ***
Documentation    Review of the different modules of the PSU.

Library       ../Libraries/PowerSupplyUnitWrapper.py
Library       ../../Commons/RobotFrameworkUtilities.py
Force Tags    psu-tests

*** Test Cases ***
Validate psu initialization
    [Documentation]    Validate psu initialization
    [Tags]    psu-initialization  command
    ${result}=  powersupplyunit initialize
    Should Be True  ${result} 

Validate psu version
    [Documentation]    Compare the model and version 
    ...                of the current psu
    [Tags]    psu-version  command
    ${psu_version}=  get powersupplyunit version
    Should Be Equal As Strings  ${psu_version}  18.52

Validate psu ac voltage
    [Documentation]    Verify that the psu ac voltage 
    ...                does not exceed 300 volts
    [Tags]    psu-ac  command
    ${psu_ac_volts}=  get powersupplyunit acvolt
    ${result}=  should be less than  ${psu_ac_volts}  300
    Should Be True  ${result}

Validate psu internal battery voltage
    [Documentation]    Validate that the psu dc voltage 
    ...                does not exceed 15 volts
    [Tags]    psu-dc  command
    ${psu_dc_volts}=  get powersupplyunit InternalBatteryVoltage
    ${result}=  should be less than  ${psu_dc_volts}  15
    Should Be True  ${result} 

Validate psu internal battery %
    [Documentation]    Validate that the psu dc % 
    ...                does not exceed 100%
    [Tags]    psu-%  command
    ${psu_charge}=  get powersupplyunit InternalBatteryPercentage
    ${result}=  should be less than  ${psu_charge}  100
    Should Be True  ${result} 


