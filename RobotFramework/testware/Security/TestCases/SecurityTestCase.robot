*** Settings ***
Documentation    Review of the different modules of the MSE.

Library       ../Libraries/SecurityWrapper.py
Library       ../../Commons/RobotFrameworkUtilities.py
Force Tags    mse-tests

*** Test Cases ***
Validate MSE initialization
    [Documentation]    Validate mse initialization
    [Tags]    mse-initialization  command
    ${result}=  mse initialize
    Should Be True  ${result} 

Validate psu version
    [Documentation]    Compare the model and version 
    ...                of the current MSE
    [Tags]    mse-version  command
    ${mse_version}=  get mse version
    Should Be Equal As Strings  ${mse_version}  (1, 2, 1, 0)

Validate hash command
    [Documentation]    Verify that the hash function
    [Tags]    mse-hash  command
    ${hash}=  get hash  /data/printerfiles/Imagem_Anexo_II_Item_201.png
    Should Be Equal As Strings  ${hash}  7838885eee5eb6aee6eae1c2c34c65c36e3794203b21594ebf0271d3b9dda23f45d5ce957bb34bdaad3be17598b687d5aa7c971c6d7a8fe52676d39a842e7



