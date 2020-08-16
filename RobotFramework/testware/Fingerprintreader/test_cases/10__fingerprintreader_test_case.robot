*** Settings ***
Documentation    Review of the different modules of the FingerPrint Reader.

Library       ../../commons/robot_framework_utilities.py
Library       ../libraries/FingerprintReader_wrapper.py
Force Tags    FPR-tests

*** Test Cases ***
Validate FingerPrint Reader connection
    [Documentation]    Connect with the FPR 
    [Tags]    FPR-connection  command
    ${FPR_conection}=  connect FPR
    Should Be True  ${FPR_conection} 

Validate FingerPrint Reader version
    [Documentation]    Compare the model and version 
    ...                of the FPR
    [Tags]    FPR-version  command
    ${FPR_version}=  get FPR version
    Should Be Equal As Strings  ${FPR_version}  0.2.0

Validate get Fingerprint image 
    [Documentation]    Get properly a fingerprint 
    [Tags]    FPR-Frame  command
    ${FPR_frame}=  get FPR frame
    Should be True  ${FPR_frame}


